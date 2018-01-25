from utils import shuffledData
import numpy as np


class Perceptron:
    def __init__(self, w=0, b=0, learn_rate=1):
        self.w = np.array(w)
        self.b = int(b)
        print("Default values: w={}, b={}".format(self.w, self.b))
        self.learn_rate = learn_rate
        self.need_shuffle = False

    def compute(self, data):
        for temp_data in data:
            x_i = [int(i) for i in temp_data[:-1]]
            x_i = np.array(x_i)
            label_i = int(temp_data[-1])
            # if temp_data is note error classicfy data, pass
            if self.dataCanUse(x_i, label_i):
                # w += LEARN_RATE * label_i * x_i
                self.updateW(label_i, x_i)
                # b += LEARN_RATE * label_i
                self.updateB(label_i)
                self.need_shuffle = True
        if self.need_shuffle:
            data = shuffledData(data)
            self.need_shuffle = False
        else:
            return self.w, self.b
        return self.compute(data)

    def dataCanUse(self, x_i, label_i):
        if (sum(self.w * x_i) + self.b) * label_i <= 0:
            return True
        else:
            return False

    def updateW(self, label_i, x_i):
        x_i = np.array(x_i)
        self.w = self.w + self.learn_rate * label_i * x_i

    def updateB(self, label_i):
        self.b += self.learn_rate * label_i

