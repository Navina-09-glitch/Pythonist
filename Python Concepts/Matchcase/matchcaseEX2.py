wkd=input("enter weekday")
match(wkd.upper()):
    case "MONDAY":
        print("{} is working day".format(wkd))
    case "TUESDAY":
        print("{} is working day".format(wkd))
    case "WEDNESSDAY":
        print("{} is working day".format(wkd))
    case "THURSDAY":
        print("{} is working day".format(wkd))
    case "FRIDAY":
        print("{} is working day".format(wkd))
    case "SATURDAY":
        print("{} is weekend".format(wkd))
    case "SUNDAY":
        print("{} is Holiday".format(wkd))
    case _:
        print("Sorry, please enter a valid choice")
