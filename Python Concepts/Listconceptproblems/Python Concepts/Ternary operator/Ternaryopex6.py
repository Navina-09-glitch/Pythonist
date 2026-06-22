x=input("enter a character:")
res="vowel" if x in ["A","E","I","O","U","a","e","i","o","u"] else "consonant"
print("{} is {}".format(x,res))