line=input("Enter a line of text: ")
words=line.split()
print(words)
el={word:len(word) for word in words if len(word)%2==0}
ol={word:len(word) for word in words if len(word)%2!=0}
print("Even length words")
for w,wl in el.items():
    print("\t{}\t\t{}".format(w,wl))

print("Odd length words")
for w,wl in ol.items():
    print("\t{}\t\t{}".format(w,wl))

#Here according to word, word length varies based on these changes we are storing it in el which is mutable
#as tuple is immutable, we cannot add these changing data to tuple so we dont have tuple comprehension

