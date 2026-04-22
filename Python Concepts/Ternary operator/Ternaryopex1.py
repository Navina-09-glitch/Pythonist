value=input("Enter the value")
res="Palindrome" if value==value[::-1] else "Not Palindrome"
print("{} is {}".format(value,res))