hour=int(input("Enter the no. of hours they worked :-"))
if(hour==8):
    print("Wage=400")
elif(hour>8 & hour<=12  ):
    wage=400+100*(hour-8)
    print("Wage = ",wage)
elif(hour>12 & hour<=16  ):
    wage=400+200*(hour-8)
    print("Wage = ",wage)
elif(hour>16 & hour<=20 ):
    wage=400+400*(hour-8)
    print("Wage = ",wage)
elif(hour>20 & hour<=24):
    wage=400+1000*(hour-8)
    print("Wage = ",wage)

