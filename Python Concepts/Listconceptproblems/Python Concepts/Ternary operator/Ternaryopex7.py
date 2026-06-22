x=input("enter a character")
res="vowel" if x in tuple("AEIOUaeiou") else "Not Vowel"
print("{} is {}".format(x,res))
