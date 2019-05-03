import numpy as n
from sklearn import preprocessing

input_labels = ['red','black','red','green','black','yellow','while']
encoder = preprocessing.LabelEncoder()
encoder.fit(input_labels)

print("\nLabel mapping:")
for i,item in enumerate(encoder.classes_):
    print(item, '-->', i)

test_label = ['green', 'red', 'black']
encoded_values = encoder.transform(test_label)
print("\nLabel =", test_label)
print("Encoded values =", list(encoded_values))

encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)
print("Decoded labels =", list(decoded_list))