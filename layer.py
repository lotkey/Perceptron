import numpy as np
import random
from node import Node

class Layer:
    # int size
    # node[] nodes
    # double rate

    def __init__(self, size, rate):
        self.rate = rate
        self.size = size       
        self.nodes = []
        for i in range(0, size):
            self.nodes.append(Node())

    def predict(self, attributes):
        if not self.size == len(attributes):
            print("Error. Size mismatch in predicting.")
            print("self.size: " + self.size)
            print("len(attributes): " + len(attributes))
            return None
        else:
            total = 0
            for i in range(0, len(attributes)):
                total += self.nodes[i].getResult(attributes[i])
            return total

    def answer(self, attributes):
        if self.predict(attributes) > .5:
            return 1
        else:
            return 0

    def printLayer(self):
        for i in range(0, self.size):
            print(self.nodes[i].getWeight())

    def getD(self, classInt):
        # returns -1 or 1
        # classInt is 0 or 1
        return classInt * 2 - 1

    def updateWeights(self, classInt, attributes):
        if not self.size == len(attributes):
            print("Error. Size mismatch in updating weights.")
            print("self.size: " + self.size)
            print("len(attributes): " + len(attributes))
        else:
            for i in range(0, self.size):
                self.nodes[i].updateWeight(attributes[i], self.rate, self.getD(classInt))
