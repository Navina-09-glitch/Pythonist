#Ducknumber is A duck number is defined as a positive integer that includes one or more zeros, excluding leading zeros. This means:
#Zeros must appear after the first digit.
#Numbers like 1023, 705, or 8900 are duck numbers.
#Numbers like 0123, 0034, or 0009 are not duck numbers because they start with zero.
# In Python, we cannot directly iterate over an integer because it's not a sequence type.
# To check each digit of a number (like for finding zeros), we convert the number to a string.
# Strings are iterable, so we can loop through each character (digit) one by one.
# Example: num = 1023 → str(num) = "1023" → we can check each digit using a for loop.
n=input("Enter the number:")
if(n[0]=="0"):
    print("{} is not duck number".format(n))
else:
    res="Not Duck number"
    for i in n:
        if(n=="0"):
            res="Duck"
            break
    print("{} is {}".format(n,res))