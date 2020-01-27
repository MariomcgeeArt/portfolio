import random
import sys 




def rearrange_quote(words):
    random.shuffle(words)
    length = len(words)
    for i in range(0,length):
        print(words[i])


rearrange_quote(sys.argv[1:])






  



