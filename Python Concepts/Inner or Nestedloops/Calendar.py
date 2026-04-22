#lines to print one month
#import calendar as kvr
#print(kvr.month(theyear=1997,themonth=9))
#line to print whole year calendar#
import calendar
Year=int(input("Enter the year:"))
if(Year<=0):
    print("Invalid Year")
else:
    print("The year is {}".format(Year))
    for i in range(1,13):
        print(calendar.month(Year,i))
