"""calculator aplication"""
print("choose an opeartion")
print("1.Add")
print("2.substraction")
print("3.Multiplication")
print("4.divide")
option=int(input("enter the opeartion"))
if option in [1,2,3,4]:
    num1=int(input("enter the number1"))
    num2=int(input("enter the number2"))
    if option==1:
        result=num1+num2
    elif option==2:
        result=num1-num2
    elif option==3:
        result=num1*num2
    elif option==4:
        result=num1//num2
    

else:
    print("enter valid option")
print("the resut is {} ".format(result))