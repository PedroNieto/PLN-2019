from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import ParameterGrid
from sklearn import metrics


from nltk.corpus import stopwords
from sentiment.tokenizer import CustomTokenizer

classifiers = {
    'maxent': LogisticRegression,
    'mnb': MultinomialNB,
    'svm': LinearSVC,
}

param_grid = [{
        'clf__C': [2**-4,2**-3,2**-2,2**-1,2**0,2**1,2**2,2**3,2**4, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000],
        'clf__penalty': ['l2'],
        'clf__dual': [True, False],
    },{
        'clf__C': [2**-4,2**-3,2**-2,2**-1,2**0,2**1,2**2,2**3,2**4, 0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000],
        'clf__penalty': ['l1'],
        'clf__dual': [False],
    }]


class SentimentClassifier(object):

    def __init__(self, clf='svm'):
        """
        clf -- classifying model, one of 'svm', 'maxent', 'mnb' (default: 'svm').
        """
        self._clf = clf
        tokenizer = CustomTokenizer()
        vectorizer = CountVectorizer(binary=True, tokenizer=tokenizer.tokenize)
        self._pipeline = pipeline = Pipeline([
            ('vect', vectorizer),
            ('clf', classifiers[clf]()),
        ])

    def fit(self, X, y, X_dev, y_dev):
        params_list = list(ParameterGrid(param_grid))        
        best_params = {}
        best_acc = 0
        for params in params_list:
            self._pipeline.set_params(**params)
            self._pipeline.fit(X, y)
            result = self.eval(self._pipeline, X_dev, y_dev)
            if result['acc'] > best_acc:
                best_acc = result['acc']
                best_params = params
        self._pipeline.set_params(**best_params)
        self._pipeline.fit(X, y)

    def predict(self, X):
        return self._pipeline.predict(X)

    
    def eval(self, model, X, y_true):
        y_pred = model.predict(X)
        acc = metrics.accuracy_score(y_true, y_pred)
        f1 = metrics.f1_score(y_true, y_pred, average='macro')
        return {'acc': acc, 'f1': f1}