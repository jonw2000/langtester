__author__ = 'jonwilliams'

import langtester.translations as datareader


datareader.read("../data.txt")


if __name__ == "__main__":
    num_translations = len(datareader.polish_english)

    
    while True:
        pol, eng = datareader.random_polish()
        answer = raw_input(pol + " > ").lower()
        if answer == 'exit':
            break
        else:
            if answer == eng.lower():
                print "Yes!"
            else:
                print "No, it was " + eng