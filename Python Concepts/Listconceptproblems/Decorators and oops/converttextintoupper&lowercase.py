def converttolowercase(kvr):
    def convertcase():
        line,upr=kvr()
        lrc=line.lower()
        return line,upr,lrc
    return convertcase

def converttouppercase(hyd):
    def convertcase():
            line=hyd()
            uc=line.upper()
            return line,uc
    return convertcase

@converttolowercase
@converttouppercase
def getline():
    line=input("Enter a line of text:")
    return line
#Main Program
line,upr,lrc=getline()
print("Given line is {}".format(line))
print("Given line is {}".format(lrc))
print("Given line is {}".format(upr))