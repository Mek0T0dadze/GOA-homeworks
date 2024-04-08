#1

academy=input("which academy are you learning: ")

if academy=="GOA":
    print("you made good choise")
else:
    print("you made wrong choise")

#2

price=int(input("enter the price of the item: "))
budget=int(input("enter your budget: "))

if budget>=price:
    print("your money is enough")
else:
    print("you dont have enough money")

#3
num1=int(input("enter num1: "))

if num1>=5:
    print(num1*2)
else:
    print(num1*4)

#4
value=10
ticket=int(input("how many ticket do you want to buy? "))

if ticket<=5:
    print(5*10)
else:
    print(ticket*100/30)

#5
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
operation=(input("enter operation: "))

if operation=="-":
    print(num1-num2)
elif operation=="+":
    print(num1+num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)