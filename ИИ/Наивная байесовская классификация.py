import numpy as np
import matplotlib as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split, cross_val_score
from utilities import visualize_classifier

input_file = 'data_multivar_nb.txt'
data = np.loadtxt(input_file, delimiter = ',')
x, y = data[:, :-1], data[:, -1]
classifier = GaussianNB()
classifier.fit(x, y)
y_pred = classifier.predict(x)

#Качество классификатора
accuracy = 100.0 * (y == y_pred).sum()/x.shape[0]
print("Качество наивной байесовского классификации = ", round(accuracy, 2), '%')
visualize_classifier(classifier, x, y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 3)
classifier_new = GaussianNB()
classifier_new.fit(x_train,y_train)
y_test_pred = classifier_new.predict(x_test)
accuracy = 100.0 * (y_test == y_test_pred).sum()/x.shape[0]
print("Качество классификации = ", round(accuracy, 2), '%')
visualize_classifier(classifier_new, x_test, y_test)

num_folds = 3
accuracy_values = cross_val_score(classifier, x, y, scoring = 'accuracy', cv = num_folds)
print('Качество: ', str(round(100*accuracy_values.mean(), 2)) + '%')
precision_values = cross_val_score(classifier, x, y, scoring = 'precision_weighted', cv = num_folds)
print('Точность: ', str(round(100*precision_values.mean(), 2)) + '%')
recall_values = cross_val_score(classifier, x, y, scoring = 'recall_weighted', cv = num_folds)
print('Полнота: ', str(round(100*recall_values.mean(), 2)) + '%')
f1_values = cross_val_score(classifier, x, y, scoring = "f1_weighted", cv = num_folds)
print('F1: ', str(round(100*f1_values.mean(), 2)) + '%')