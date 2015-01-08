#qpy:console

__author__ = 'jonwilliams'
import os, sys
import langtester.translations as datareader

#import androidhelper
path = os.path.dirname(os.path.realpath(sys.argv[0]))
#droid = androidhelper.Android()
datareader.read(path + "/storage/emulated/0/com.hipipal.qpyplus/projects/langtester/data.txt")

#droid.makeToast('Langtester')

if __name__ == "__main__":
    num_translations = len(datareader.polish_english)

    lastans = ""
    correct = 0
    wrong = 0
    while True:
    
        pol, eng = datareader.random_polish()
        
        answer = raw_input(lastans + '\n' + pol + " > ")
        #answer = droid.dialogGetInput(lastans + ", correct: " + str(correct) + " wrong: " + str(wrong), pol)
        
        answer = answer.strip().lower()
        if not answer or answer == 'exit':
            break
        else:
            if answer == eng.lower():
                lastans = "Correct"
                correct = correct + 1
            else:
                lastans = "No, it was " + eng
                wrong = wrong + 1
                
    exit