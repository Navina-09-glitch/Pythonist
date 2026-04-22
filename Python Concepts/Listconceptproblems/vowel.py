word=input("Enter a word: ")
if(len(word)==0):
    print("Empty word")
else:
    if(word.isspace()):
        print("word should not be space")
    else:
        res="NOT VOWEL WORD"
        for ch in word:
            if ch.lower() in list("aeiou"):
                res="VOWEL WORD"
                break
        print("{} is {}".format(res,word))