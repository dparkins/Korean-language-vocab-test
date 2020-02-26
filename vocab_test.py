#Quick script to test me on my Korean vocab
from numpy import random
import numpy as np
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
    length_test = 10
    k = random.choice(n,length_test)
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
            print("Correct!")
        else:
            failure +=1
            print("Incorrect")

    print("You got {0:} out of {1:} correct".format(success,length_test))
    if np.float32(success)/np.float32(length_test) > 0.6:
        print("Well done")
    else:
        print("Try again")
