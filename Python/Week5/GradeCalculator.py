numberGrade = int(input("Enter Your Grade: "))

if(numberGrade >= 90):
    print("You Got An A, Great Job!")
elif(80 <= numberGrade <= 89):
    print("You Got An B, pretty decent")
elif(70 <= numberGrade <= 79):
    print("You Got a C, barely a pass")
elif(60 <= numberGrade <= 69):
    print("You Got a D, watch out!")
elif(numberGrade <= 59):
    print("You Got a F, better luck next time!")