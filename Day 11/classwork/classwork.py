num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))
operation=input("enter operation: ")

if operation=="*":
    print(num1*num2*num3)
elif operation=="-":
    print(num1-num2-num3)
elif operation=="+":
    print(num1+num2+num3)
elif operation=="/":
    print(num1/num2/num3)
else:
    print("your operaton is not right")
