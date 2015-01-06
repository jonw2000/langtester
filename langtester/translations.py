__author__ = 'jonwilliams'

import random

polish_english = {}
english_polish = {}

def read(filename):
    file_obj = open(filename, 'r')
    for line in file_obj:
        stripped = unicode(line.strip(), 'utf8')
        if len(stripped) > 0 and stripped[0] != '#':
            polish = stripped.split('-')[0].strip()
            english = stripped.split('-')[1].strip()
            polish_english[polish] = english
            english_polish[english] = polish

def print_polish():
    for pol, eng in polish_english.items():
        print pol + ":" + eng

def print_english():
    for eng, pol in english_polish.items():
        print eng + ":" + pol

def size():
    return len(polish_english)

def random_polish():
    pol = random.choice(polish_english.keys())
    eng = polish_english[pol]
    return pol, eng

