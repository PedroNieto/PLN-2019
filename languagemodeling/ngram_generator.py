from collections import defaultdict
import random
import operator


class NGramGenerator(object):

    def __init__(self, model):
        """
        model -- n-gram model.
        """
        self._n = model._n

        # compute the probabilities
        probs = defaultdict(dict)

        for key in model._count:
            if(len(key) == self._n):
                token = key[self._n-1]
                prev_token = key[0:self._n - 1]
                probs[prev_token][token] = model.cond_prob(token, prev_token)


        self._probs = dict(probs)

        # sort in descending order for efficient sampling
        self._sorted_probs = sorted_probs = {}
        for key, value in probs.items():
            sorted_list = sorted(value.items(), key=operator.itemgetter(1), reverse=True)
            sorted_probs[key] = sorted_list

    def generate_sent(self):
        """Randomly generate a sentence."""
        word = '<s>'
        sent = [word] * (self._n - 1)
        i = 0
        while word != '</s>':
            prev_token = tuple(sent[i : i + self._n - 1])
            word = self.generate_token(prev_token)
            sent.append(word)
            i += 1
        sent = sent[self._n - 1 : len(sent) -1]
        return sent

    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.

        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        if self._n > 1 and prev_tokens is None:
            raise Exception("Missing Argument")

        r = random.random()
        key = ()
        if self._n > 1:
            key = prev_tokens
        probs = self._sorted_probs[key]

        i = 0
        word, prob = probs[i]
        acum = prob
        aux = 0

        while r > acum:
            i += 1
            word, prob = probs[i]
            acum += prob

        return word
