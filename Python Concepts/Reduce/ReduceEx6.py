#Program for getting line of Text from list of words
import functools #predefined module
lst=list(map(str,input("Enter list of words separated by comma:").split(",")))
print("Given Words:")
print(lst)
line=functools.reduce(lambda k,v:k+" "+v,lst)
print("Line of Text:")
print(line)