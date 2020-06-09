from translator import Translator
from layer import Layer

translator = Translator()
data = translator.getData()
training = data[0]
for i in range(0, len(training)):
    if len(training) - 1 >= i and len(training[i]) == 0:
        del training[i]
testing = data[1]
for i in range(0, len(testing)):
    if len(testing) - 1 >= i and len(testing[i]) == 0:
        del testing[i]

layer = Layer(len(training[0]) - 1, .2)
for h in range(0, 1000):
    for i in range(0, len(training)):
        classInt = training[i][0]
        attributes = training[i][1:len(training[i])]

        if not layer.answer(attributes) == classInt:
            layer.updateWeights(classInt, attributes)

layer.printLayer()

correct = 0.0
total = 0.0
for i in range(0, len(testing)):
    classInt = testing[i][0]
    attributes = testing [i][1:len(training[i])]

    if layer.answer(attributes) == classInt:
        correct += 1
    total += 1

print("Correct: " + str(correct/total))
