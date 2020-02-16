
import Alphabet
from tensorflow.keras.models import load_model
import pickle

import numpy


def find(elem):
    for char in Alphabet.Alphabet:
        if char.value == elem:
            return char.name

def guess(WordsName, model):
    model = load_model(model)
    IMG_SIZE = 28

    pickle_in = open(WordsName, "rb")
    elements = pickle.load(pickle_in)
    pickle_in.close()
    elements = numpy.array(elements).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

    wp = model.predict(elements)
    c = 0
    prop = []
    fl = True
    task_number = 0
    file = open('/'.join(WordsName.split('/')[:-1]) + '/exit.txt', 'w')
    while True:
        if find(numpy.argmax(wp[c])) == 'Замена':
            fl = False
        if find(numpy.argmax(wp[c])) == 'Пробел':
            fl = False
        if fl:
            prop.append(find(numpy.argmax(wp[c])))
        fl = True
        if c % 23 == 0 and not c == 0:
            task_number += 1
            s = ''.join(prop)
            file.write(s.lower())
            file.write('\n')
            prop.clear()
        if c > len(wp)-2:
            break
        c += 1
    file.close()
