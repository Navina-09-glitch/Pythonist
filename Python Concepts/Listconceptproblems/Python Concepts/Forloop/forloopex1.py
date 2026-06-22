s=input("enter line of text:")
print("by using for loop--- forward direction")
for ch in s:
    print(ch)
print("-"*50)
for i in range(len(s)):
    print(s[i])
print("-"*50)
for i in range(-len(s),0):
    print(s[i])
print("-"*50)
print("by using loop--- backward direction")
for ch in s[::-1]:
    print(ch)
for i in range(len(s)-1,-1,-1):
    print(s[i])
print("-"*50)
for i in range(-1,-(len(s)+1),-1):
    print(s[i])
print("-"*50)

