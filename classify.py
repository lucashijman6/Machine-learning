from machinelearningdata import Machine_Learning_Data
import main as glob
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

# LESBRIEF Deel 2
# SUPERVISED LEARNING
data = Machine_Learning_Data(glob.student_number)

# haal data op voor classificatie
classification_training = data.classification_training()

# extract de data x = array met waarden, y = classificatie 0 of 1
X = glob.extract_from_json_as_np_array("x", classification_training)

# dit zijn de werkelijke waarden, daarom kan je die gebruiken om te trainen
Y = glob.extract_from_json_as_np_array("y", classification_training)

# Plot data
for i in range(len(X)):
    plt.plot(X, Y, "k.")

plt.show()

# TODO: leer de classificaties
clf1 = GaussianNB()
clf1.fit(X, Y)

clf2 = LogisticRegression()
clf2.fit(X, Y)

# TODO: voorspel na het trainen de Y-waarden (je gebruikt hiervoor dus niet meer de
#       echte Y-waarden, maar enkel de X en je getrainde classifier) en noem deze
#       bijvoordeeld Y_predict
predicted_y_1 = clf1.predict(X)
predicted_y_2 = clf2.predict(X)

# Plot het resultaat van classifier 1
for i in range(len(X)):
    plt.plot(X, predicted_y_1, "k.")

plt.show()

# Plot het resultaat classifier 2
for i in range(len(X)):
    plt.plot(X, predicted_y_2, "k.")

plt.show()

# TODO: vergelijk Y_predict met de echte Y om te zien hoe goed je getraind hebt
# correct_guesses = []
# for i in range(len(predicted_y)):
#     if(predicted_y[i] == Y[i]):
#         correct_guesses.append(predicted_y[i])

# print("Classificatie accuratie (echte Y): " + str(len(correct_guesses) / len(Y)))

accuracies = [accuracy_score(Y, predicted_y_1, normalize=False), accuracy_score(Y, predicted_y_2, normalize=False)]

for i in range(len(accuracies)):
    plt.plot(0, accuracies[i], "k.")

plt.show()

# haal data op om te testen
classification_test = data.classification_test()
# testen doen we 'geblinddoekt' je krijgt nu de Y's niet
X_test = glob.extract_from_json_as_np_array("x", classification_test)

# TODO: voorspel na nog een keer de Y-waarden, en plaats die in de variabele Z
#       je kunt nu zelf niet testen hoe goed je het gedaan hebt omdat je nu
#       geen echte Y-waarden gekregen hebt.
#       onderstaande code stuurt je voorspelling naar de server, die je dan
#       vertelt hoeveel er goed waren.

Z_1 = clf1.predict(X_test)
Z_2 = clf2.predict(X_test)

for i in range(len(X_test)):
    plt.plot(X_test, Z_1, "k.")

plt.show()

for i in range(len(X_test)):
    plt.plot(X_test, Z_2, "k.")

plt.show()

# stuur je voorspelling naar de server om te kijken hoe goed je het gedaan hebt
# tolist zorgt ervoor dat het numpy object uit de predict omgezet wordt naar een 'normale' lijst van 1'en en 0'en
classification_test_1 = data.classification_test(Z_1.tolist())
classification_test_2 = data.classification_test(Z_2.tolist())

test_results = [classification_test_1, classification_test_2]

for i in range(len(test_results)):
    plt.plot(0, test_results[i], "k.")

plt.show()

print("Classificatie accuratie (test): " + str(classification_test_1))
print("Classificatie accuratie (test): " + str(classification_test_2))