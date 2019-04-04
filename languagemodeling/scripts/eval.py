"""Evaulate a language model using a test set.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Language model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import math

from nltk.corpus import PlaintextCorpusReader


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the model
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    # load the data
    # LOAD YOUR EVALUATION CORPUS
    corpus = PlaintextCorpusReader('../../textos/', 'out.txt')
    eval_sents = corpus.sents()[int(len(corpus.sents())*0.9):]

    # compute the cross entropy
    log_prob = model.log_prob(eval_sents)
    e = model.cross_entropy(eval_sents)
    p = model.perplexity(eval_sents)

    print('Log probability: {}'.format(log_prob))
    print('Cross entropy: {}'.format(e))
    print('Perplexity: {}'.format(p))
