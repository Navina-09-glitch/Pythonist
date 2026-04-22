#Program for accepting line of Text and get those words which contains atleast one vowel
def findvowel(word):
    res=False
    for ch in word:
        if ch.lower() in list("aeiou"):
            res=True
            break
    return res
#Main Program
line=input("Enter line of text:")
words=line.split()
vwords=list(filter(findvowel,words))
print(vwords)