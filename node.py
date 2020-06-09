import random
import numpy as np

class Node:
    # double weight

    def __init__(self):
        self.weight = random.uniform(0, 1)

    def getResult(self, attribute):
        return self.weight * attribute

    def updateWeight(self, attribute, learningRate, d):
        self.weight = self.weight + learningRate * d * attribute

    def getWeight(self):
        return self.weight
