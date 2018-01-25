#!/usr/bin/env python

from PerceptronOriginalForm import Perceptron
from utils import loadData

def main():
    data = loadData('./data.txt')
    per = Perceptron(0, 0, 1)
    w, b = per.compute(data)
    print('Result Output: w={}, b={}'.format(w, b))

if __name__ == '__main__':
    main()
