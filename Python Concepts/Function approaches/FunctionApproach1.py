Input: Taking from function call
Process: Inside Function body
Output: Giving to Function call

#Function Definition
def sumop(k,v):# here k,v are called formal parameters
    r=k+v    #r is called local variable
    return r

#Main Program
#First use of function

x=float(input("Enter First number"))
y=float(input("Enter Second number"))
res=sumop(x,y) #Function call
print("sum({},{})={}".format(x,y,res))

#Second use of function
k=float(input("Enter first number"))
v=float(input("Enter second number"))
r=sumop(k,v) #Function call
print("sum({},{})={}".format(k,v,r))