#1
num=int(input("enter num: "))

for i in  range(0, num+1):
    print (i)

#2
count_numbers = int(input("Please enter how many numbers do you want to input: "))

sum_numbers = 0

for i in range(1, count_numbers + 1):
    user_num = int(input("Please enter number " + str(i) + ": "))
    sum_numbers = sum_numbers + user_num


#3
result=0
i=0

while i<=20:
    print(i)
    i=i+2
    

fruits=("cherry", "apple", "peach")
for i in fruits:
    print(i)