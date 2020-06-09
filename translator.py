import numpy as np
import random

class Translator:
    # string fileName
    # int[] info
    # char[] classNames
    # char[] answerNames

    def __init__(self, file = "data.data"):
        self.fileName = file
        
        infile = open(file, "r")
        lines = infile.read().split("\n")

        for i in range(0, len(lines)):
            lines[i] = lines[i].split(",")
        del lines[i]

        lines = np.asarray(lines)
        self.classNames = []
        classes = lines[:,0]
        while(len(classes) != 0):
            self.classNames.append(classes[0])
            classes = classes[classes != classes[0]]

        self.answerNames = []
        answers = lines[:,range(1, len(lines[0]))]
        for i in range(0, len(answers)):
            for j in range(0, len(answers[i])):
                if not answers[i][j] in self.answerNames:
                    self.answerNames.append(answers[i][j])

        self.info = [[]]

        for i in range(0, len(lines)):
            line = []
            line.append(self.classNames.index(lines[i][0]))
            for j in range(1, len(lines[i])):
                line.append(self.answerNames.index(lines[i][j]) + 1)
            self.info.append(line)

    def getData(self):
        data = self.info
        random.shuffle(data)

        offset = 0
        for i in range(0, len(data)):
            if len(data[i - offset]) == 0:
                del data[i - offset]
                offset += 1

        index = int(len(data) * .8)

        training = data[0:index]
        testing = data[index:len(data)]

        return (training, testing)
        
