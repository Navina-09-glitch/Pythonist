#Program for accepting line of text and get those words which contains atleast one vowel
line=input("Enter line of text:") #Sky is Blue
words=line.split() #words=[Sky,is,Blue]
vwords=list(filter(lambda word:not(set(word.lower()).isdisjoint(set("aeiou"))),words))
print("Vowel Words",vwords)