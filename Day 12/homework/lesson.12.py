#1

num=int(input("enter num: "))

for i in range(11):
    print(i)
if num%2==1:
    print("the number is odd")
else:
    print("the number is not odd")


#2
for i in range(51):
    print(i)

num=int(input("enter num: "))
if num==5:
    print(5%5)
elif num==10:
    print(10%5)
elif num==15:
    print(15%5)
elif num==20:
    print(20%5)
elif num==25:
    print(25%5)
elif num==30:
    print(30%5)
elif num==35:
    print(35%5)
elif num==40:
    print(40%5)
elif num==45:
    print(45%5)
elif num==50:
    print(50%5)
else:
    print("this number is not a multiple of 5")

#3
num=int(input("enter num: "))
for num in range(num):
    print(num)


#4
num=0
for i in range(51):
   num=+i
print(num)