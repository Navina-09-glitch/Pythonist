wkd=input("Enter a weekname")
if wkd.upper() in ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY","MON","TUE","WED","THU","FRI","SAT","SUN"]:
        match(wkd[0:3].upper()):
            case "MON" | "TUE" | "WED" | "THU" | "FRI":
                print("{} is working day".format(wkd))
            case "SAT":
                print("{} is weekend".format(wkd))
            case "SUN":
                print("{} is Holiday".format(wkd))
else:
    print("{} is not a weekday".format(wkd))