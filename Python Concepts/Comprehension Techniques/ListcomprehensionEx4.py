#write an python program which will accept a line of text and get even length and odd
#length words separately

line=input("Enter line of Text:")
words=line.split()
print(words)
el=[]
ol=[]
for word in words:
    if(len(word)%2==0):
        el.append(word+":"+str(len(word)))
#If along with word ,I want word length then I use + with str
    else:
        ol.append(word+":"+str(len(word)))
print("Even length words {}".format(el))
print("Odd length words {}".format(ol))


#Using list comprehension
line1=input("Enter line of Text:")
words1=line1.split()
print(words1)
el=[word+":"+str(len(word)) for word in words1 if len(word)%2==0]
ol=[word+":"+str(len(word)) for word in words1 if len(word)%2!=0]
print("Even length words {}".format(el))
print("Odd length words {}".format(ol))