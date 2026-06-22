#Program for getting line of text from list of words
import functools #predefined module
def kvrjoin(k,v):
    return (k+" "+v)
#Main Program
lst=list(map(str,input("Enter list of words separated by comma:").split(",")))
print("Given Words:")
print(lst)
line=functools.reduce(kvrjoin,lst)
print("line of text:")
print(line)