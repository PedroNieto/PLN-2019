# https://docs.python.org/3/library/collections.html
from collections import defaultdict
import math
import random


class LanguageModel(object):

    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.

        sent -- the sentence as a list of tokens.
        """
        return 0.0

    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        return -math.inf

    def log_prob(self, sents):
        """Log-probability of a list of sentences.

        sents -- the sentences.
        """
        result = 0
        for sent in sents:
            result += self.sent_log_prob(sent)
        return result

    def cross_entropy(self, sents):
        """Cross-entropy of a list of sentences.

        sents -- the sentences.
        """
        word_count = sum(map(len, sents))

        log_prob = self.log_prob(sents)
        return - log_prob / word_count


    def perplexity(self, sents):
        """Perplexity of a list of sentences.

        sents -- the sentences.
        """
        cross_entropy = self.cross_entropy(sents)
        return 2 ** cross_entropy


class NGram(LanguageModel):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        assert n > 0
        self._n = n

        count = defaultdict(int)

        for sent in sents:
            sent.append('</s>')
            sent = ['<s>'] * (n-1) + sent
            for i in range(len(sent) - n + 1):
                ngram = tuple(sent[i:i+n])
                ngram2 = tuple(sent[i:i+n-1])
                count[ngram] += 1
                count[ngram2] += 1
        self._count = dict(count)


    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.

        tokens -- the n-gram or (n-1)-gram tuple.
        """
        return self._count.get(tokens, 0)

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        if self._n > 1 and prev_tokens is None:
            raise Exception("Missing Argument")

        prev_tuple = ()
        if prev_tokens != None:
            prev_tuple = prev_tokens
        tuple = prev_tuple + (token,)

        token_count = self.count(tuple)
        prev_count = self.count(prev_tuple)
        if prev_count == 0:
            return 0

        prob = token_count / prev_count
        return prob

    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.

        sent -- the sentence as a list of tokens.
        """
        n = self._n
        sent.append('</s>')
        sent = ['<s>'] * (n - 1) + sent

        result = 1
        for i in range(len(sent) - n + 1):
            result *= self.cond_prob(sent[i + n -1] , tuple(sent[i:i + n -1]))
        return result


    def sent_log_prob(self, sent):
        """Log-probability of a sentence.

        sent -- the sentence as a list of tokens.
        """
        n = self._n
        sent.append('</s>')
        sent = ['<s>'] * (n - 1) + sent

        result = 0
        for i in range(len(sent) - n + 1):
            prob = self.cond_prob(sent[i + n -1], tuple(sent[i:i + n -1]))
            if prob == 0:
                return -math.inf
            result += math.log(prob, 2)
        return result




class AddOneNGram(NGram):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        # call superclass to compute counts
        super().__init__(n, sents)

        # compute vocabulary
        self._voc = voc = set()
        for sent in sents:
            for word in sent:
                voc.add(word)

        self._V = len(voc)  # vocabulary size

    def V(self):
        """Size of the vocabulary.
        """
        return self._V

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """

        if self._n > 1 and prev_tokens is None:
            raise Exception("Missing Argument")

        prev_tuple = ()
        if prev_tokens != None:
            prev_tuple = prev_tokens
        tuple = prev_tuple + (token,)

        token_count = self.count(tuple) + 1
        prev_count = self.count(prev_tuple) + self.V()
        prob = token_count / prev_count
        return prob

class InterpolatedNGram(NGram):

    def __init__(self, n, sents, gamma=None, addone=True):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        gamma -- interpolation hyper-parameter (if not given, estimate using
            held-out data).
        addone -- whether to use addone smoothing (default: True).
        """
        assert n > 0
        self._n = n
        if gamma is not None:
            # everything is training data
            train_sents = sents
        else:
            # 90% training, 10% held-out
            m = int(0.9 * len(sents))
            train_sents = sents[:m]
            held_out_sents = sents[m:]

        print('Computing counts...')
        # COMPUTE COUNTS FOR ALL K-GRAMS WITH K <= N
        count = defaultdict(int)

        for sent in train_sents:
            sent.append('</s>')
            for j in range(1,n + 1):
                aux_sent = ['<s>'] * (j-1) + sent
                for i in range(len(aux_sent) - j + 1):
                    count[tuple(aux_sent[i:i+j])] += 1
                    if j == 1:
                        count[tuple(aux_sent[i:i+j-1])] += 1

        self._count = dict(count)



        # compute vocabulary size for add-one in the last step
        self._addone = addone
        if addone:
            print('Computing vocabulary...')
            self._voc = voc = set()
            for sent in sents:
                voc.update(sent)


        # compute gamma if not given
        if gamma is not None:
            self._gamma = gamma
        else:
            print('Computing gamma...')
            self._gamma = self.calculate_gamma(held_out_sents)
            # use grid search to choose gamma

    def calculate_gamma(self, held_out_sents):
        best_perplexity = math.inf
        best_gamma = None
        for i in range(25):
            self._gamma = 2**1
            perplexity = self.perplexity(held_out_sents)
            if perplexity < best_perplexity:
                best_perplexity = perplexity
                best_gamma = self._gamma
        return best_gamma

    def count(self, tokens):
        """Count for an k-gram for k <= n.

        tokens -- the k-gram tuple.
        """
        return self._count.get(tokens, 0)

    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.

        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        if self._n > 1 and prev_tokens is None:
            raise Exception("Missing Argument")

        prev_tuple = ()
        if prev_tokens != None:
            prev_tuple = prev_tokens
        tuple = prev_tuple + (token,)

        lambda_acum = 0
        prob = 0
        for i in range(self._n):
            l = self.calculate_lambda(tuple[i:], lambda_acum, i)
            lambda_acum += l
            if self._addone and i == self._n -1:
                prev_count = self.count(prev_tuple[i:]) + len(self._voc)
                tuple_count = self.count(prev_tuple + (token,)) + 1
            else:
                prev_count = self.count(prev_tuple[i:])
                tuple_count = self.count(prev_tuple + (token,))

            if prev_count != 0:
                prob += (l * (tuple_count / prev_count))

        return prob

    def calculate_lambda(self, tuple, lambda_acum, i):
        if i == self._n - 1:
            return 1 - lambda_acum
        else:
            return (1 - lambda_acum) * ((self.count(tuple[:self._n-1]))/(self.count(tuple[:self._n-1]) + self._gamma))

class BackOffNGram(NGram):

    def __init__(self, n, sents, beta=None, addone=True):
        """
        Back-off NGram model with discounting as described by Michael Collins.

        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        beta -- discounting hyper-parameter (if not given, estimate using
            held-out data).
        addone -- whether to use addone smoothing (default: True).
        """
        assert n > 0
        self._n = n
        if beta is not None:
            # everything is training data
            train_sents = sents
        else:
            # 90% training, 10% held-out
            m = int(0.9 * len(sents))
            train_sents = sents[:m]
            held_out_sents = sents[m:]

        print('Computing counts...')
        # COMPUTE COUNTS FOR ALL K-GRAMS WITH K <= N
        count = defaultdict(int)

        for sent in train_sents:
            aux_sent = ['<s>'] * (self._n-1) + sent
            aux_sent.append('</s>')
            for j in range(1,n + 1):
                for i in range(len(aux_sent) - j + 1):
                    count[tuple(aux_sent[i:i+j])] += 1
                    if j == 1:
                        count[tuple(aux_sent[i:i+j-1])] += 1

        self._count = dict(count)



        # compute vocabulary size for add-one in the last step
        self._addone = addone
        if addone:
            print('Computing vocabulary...')
            self._voc = voc = set()
            for sent in sents:
                voc.update(sent)


        # compute gamma if not given
        if beta is not None:
            self._beta = beta
        else:
            print('Computing gamma...')
            self._gamma = self.calculate_beta(held_out_sents)

        self._A = A = defaultdict(set)
        for kgram in self._count.keys():
            if len(kgram) >= 2:
                key_A = kgram[:-1]
                A[key_A].add(kgram[len(kgram) - 1])

    def calculate_beta(self, held_out_sents):
        pass

    """
       Todos los métodos de NGram.
    """

    def A(self, tokens):
        """Set of words with counts > 0 for a k-gram with 0 < k < n.

        tokens -- the k-gram tuple.
        """
        return self._A[tokens]

    def alpha(self, tokens):
        """Missing probability mass for a k-gram with 0 < k < n.

        tokens -- the k-gram tuple.
        """
        A = self.A(tokens)
        if len(A) > 0 and self.count(tokens) > 0:
            return (self._beta * len(A))/self.count(tokens)
        else:
            return 1


    def denom(self, tokens):
        """Normalization factor for a k-gram with 0 < k < n.

        tokens -- the k-gram tuple.
        """
        A = self.A(tokens)

        count = self.count(tokens[1:])
        sum = 0
        for word in A:
            sum += self.cond_prob(word, tokens[1:])
        return 1 - sum

    def discounted_count(self, tokens):
        return self.count(tokens) - self._beta

    def cond_prob(self, token, prev_tokens=None):
        if prev_tokens is None or prev_tokens is ():
            return self.count((token,)) / self.count(())
        if token in self.A(prev_tokens):
            discounted_count = self.discounted_count(prev_tokens + (token,))
            prev_count = self.count(prev_tokens)
            return discounted_count/prev_count
        alpha = self.alpha(prev_tokens)
        denom = self.denom(prev_tokens)
        return alpha * (self.cond_prob(token, prev_tokens[1:])/denom)
