"""Train an n-gram model.

Usage:
  train.py [-m <model>] -n <n> -o <file>
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -m <model>    Model to use [default: ngram]:
                  ngram: Unsmoothed n-grams.
                  addone: N-grams with add-one smoothing.
                  inter: N-grams with interpolation smoothing.
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle

from nltk.corpus import PlaintextCorpusReader
from nltk import download


from languagemodeling.ngram import NGram, AddOneNGram, InterpolatedNGram


models = {
    'ngram': NGram,
    'addone': AddOneNGram,
    'interpolated': InterpolatedNGram,
}


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    corpus = PlaintextCorpusReader('../../textos/', 'out.txt')
    train_sents = corpus.sents()[0:int(len(corpus.sents())*0.9)]

    # train the model
    n = int(opts['-n'])
    model_class = models[opts['-m']]
    model = model_class(n, train_sents)

    # save it
    filename = opts['-o']
    f = open(filename, 'wb')
    pickle.dump(model, f)
    f.close()
