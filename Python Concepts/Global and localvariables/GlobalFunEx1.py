a=10
b=20
c=30
d=40
#a,b,c,d are called global variables
def operation():
    x=100
    y=200
    z=300
    k=400
#x,y,z,k are called local variables
    res=x+y+z+k+a+b+c+d
    print("Sum of both and global var values=", res)

#Main Program
operation()