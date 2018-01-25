import random

def loadData(path):
    with open(path) as f:
        data = f.readlines()
        data = [[int(i) for i in temp_data.replace('\n', '').split(',')] for temp_data in data[1:]]
    return data


def shuffledData(data):
    random.shuffle(data)
    return data
