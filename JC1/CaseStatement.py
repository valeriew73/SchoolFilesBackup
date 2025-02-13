DayNum = int(input("Enter a day number between 1 and 7 (inclusive): ")) #DayNum is of data type integer
if DayNum == 1:
    print("Sunday")
elif DayNum == 2:
    print("Monday")
elif DayNum == 3:
    print("Tuesday")
elif DayNum == 4:
    print("Wednesday")
elif DayNum == 5:
    print("Thursday")
elif DayNum == 6:
    print("Friday")
elif DayNum == 7:
    print("Saturday")
else: print("Error. Invalid day number.")


#python equivalent of case statement, case _ means otherwise
match DayNum:
    case 1: print("Sunday")
    case 2: print("Monday")
    case 3: print("Tuesday")
    case 4: print("Wednesday")
    case 5: print("Thursday")
    case 6: print("Friday")
    case 7: print("Saturday")
    case _: print("Error. Invalid day number.")



