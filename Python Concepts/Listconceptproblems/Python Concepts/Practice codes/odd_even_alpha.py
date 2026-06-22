#Given data:7S6t2r5ln5G8
#a.Get all Uppercase alphabets in Descending order--SIG
#b.Get all lowercase alphabets in Ascending order---trn
#c.get all the odd number in ascending order ---557
#d.get all the even number in descending order---268
#Note: If any special symbols are there ignore them
data="7S6t2r5ln5G8"
#Separate Characters
upper=[]
lower=[]
odd=[]
even=[]
for ch in data:
    if ch.isupper():
        upper.append(ch)
    elif ch.islower():
        lower.append(ch)
    elif ch.isdigit():
        num=int(ch)
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
#Sort as per requirements
upper.sort(reverse=True) #Descending
lower.sort()   #Ascending
odd.sort()     #Ascending
even.sort(reverse=True) #Descending

#Convert list to strings
print("Uppercase Descending:","".join(upper))
print("Lowercase Ascending:","".join(lower))
print("Odd Descending:","".join(map(str,odd)))
print("Even Descending:","".join(map(str,even)))