#Quick script to test me on my Korean vocab
from numpy import random
import numpy as np
import bisect
import os
if __name__ == "__main__":
    #open vocab file
    f = open('vocab.txt','r')
    lines = f.readlines()
    english = []
    korean = []
    for line in lines:
        c = line.split(",")
        english.append(c[0])
        korean.append(c[1].strip())

    f.close()
    n = len(english)
    # check to see if '.tmp' directory exists
    dir_exists = os.path.isdir('.tmp')
    if not dir_exists:
        # create directory to store weights
        os.mkdir('.tmp/')

    #check to see if file of weights exists
    weights_exist = os.path.isfile('.tmp/vocab_weights.txt')
    if weights_exist:
        f = open('.tmp/vocab_weights.txt','r')
        lines_weights = f.readlines()
        english_weights = []
        korean_weights = []
        weights = []
        for line in lines_weights:
            c = line.split(",")
            english_weights.append(c[0])
            korean_weights.append(c[1].strip())
            weights.append(np.float(c[2]))

        f.close()
        n_weights = len(english_weights)
        if n_weights < n:
            print('Words have been added')
            for i_weights in range(n_weights,n):
                weights.append(1.0)
                
    else: #create weights file
        f = open('.tmp/vocab_weights.txt','w')
        for i in range(0,n):
            string_out = "{0:},{1:},{2:}".format(english[i],korean[i],1.0)
            f.write(string_out+"\n")

        f.close()
        weights = np.ones(n)


    total = sum(weights)
    cumulative = np.cumsum(weights)
    cumulative /= total

    length_test = 10
    #k = random.choice(n,length_test,replace=False)
    k= []
    for ik in range(length_test):
        trial = random.uniform(0,1.0)
        k_in = bisect.bisect_left(cumulative,trial)
        k.append(k_in)

    print(k)
    success = 0
    failure = 0
    for ik in k:
        print("What is the Korean word for {0:}?".format(english[ik]))
        guess = input()
        print("You wrote {0:}".format(guess))
        print("The answer is {0:}".format(korean[ik]))
        if guess == korean[ik]:
            success +=1
            weights[ik] *= 0.8
            print("Correct!")
        else:
            failure +=1
            weights[ik] *= 1.2
            print("Incorrect")

    print("You got {0:} out of {1:} correct".format(success,length_test))
    f = open('.tmp/vocab_weights.txt','w')
    for i in range(0,n):
        string_out = "{0:},{1:},{2:}".format(english[i],korean[i],weights[i])
        f.write(string_out+"\n")

    f.close()
    weights = np.ones(n)
    if np.float32(success)/np.float32(length_test) > 0.6:
        print("Well done")
    else:
        print("Try again")
