#Program for accepting line of text and get those words which contains at least one vowel
def findvowel(word):
    res=not(set(word.lower()).isdisjoint(set("aeiou")))
    return res
#Main Program
line=input("Enter line of Text")
words=line.split()
vwords=list(filter(findvowel,words))
print("Vowel words",vwords)