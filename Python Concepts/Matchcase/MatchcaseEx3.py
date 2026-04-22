wkd=input("Enter a weekname")
match(wkd.upper()):
    case "MONDAY"|"TUESDAY"|"WEDNESDAY"|"THURSDAY"|"FRIDAY"|"MON"|"TUE"|"WED"|"THU"| "FRI":
        print("{} is working day".format(wkd))
    case "SATURDAY" |"SAT":
        print("{} is weekend".format(wkd))
    case "SUNDAY"|"SUN":
        print("{} is Holiday".format(wkd))
    case _:
        print("Sorry, please enter a valid choice")