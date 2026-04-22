palindrome=lambda w:"{} is palindrome".format(w) if w==w[::-1] else "{} is not palindrome".format(w)
#Anonymous Fun without Param
word=lambda: input("Enter any name:").lower()
#Main Program
print(palindrome(word()))