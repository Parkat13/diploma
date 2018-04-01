# -*- coding: utf-8 -*-
import codecs
import pandas as pd
import numpy
from sklearn import svm
from sklearn.model_selection import cross_val_score
import random
from sklearn import metrics
table = pd.read_csv('feature.csv')
numpy.random.seed(1)
table = table.iloc[numpy.random.permutation(len(table))]
data = table.loc[:, ['C-Value'], ].values
target = table['Class'].values
for param in range(2, 3):
    numpy.random.seed()
    clf = svm.LinearSVC(random_state=4)
    scores = cross_val_score(clf, data, target, cv=7, scoring='average_precision')
    print(scores)
    print()
    print(str(scores.mean()))
#results.read_csv('results_sci-learn.csv')
#resuls.to_csv('results_sci-learn.csv')
