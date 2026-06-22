n=(input("Enter a number: "))
if(n==n[::-1]):
    print("{} is palindrome".format(n))
else:
    print("{} is not palindrome".format(n))
print("Program execution completed")