import random
wordBank=["harirrr naghshbandi","sepinoud marhamati"]
word = random.choice(wordBank).lower()
fill=[" _ "]*len(word)
if " " in word:
    fill[word.index(" ")]="   "
wrong=0

while wrong <6:
    print(' '.join(map(str, fill)))
    if " _ " not in fill:
        print("you win")
        break
    else:
        gess=input().lower()
        if gess in word:
            tempfill=word
            index=0
            while gess in tempfill:
                index+=tempfill.index(gess)+1
                tempfill=word[index:]
                fill[index-1]=gess
        else:
            print("wrong!! try again")
            wrong+=1
 
if " _ " in fill:
    print("you lose")