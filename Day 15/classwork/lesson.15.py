#1
def user_name (name):
    print("hello",name)

user_name("nika")

#2
def add(num1,num2):
    print(num1+num2)

add(1,2)

#3
def mult(num1,num2):
    print(num1*num2)

add(1,2)

#4
def add(num1, num2):
    print(num1+num2)

add(1,2)

def minus(num1, num2):
    print(num1-num2)

minus(5,2)

def multiply(num1,num2):
    print(num1*num2)

multiply(3,3)

def division(num1,num2):
    print(num1/num2)

division(10,2)

#5
def rectange_area(length, width):
    print(length*width)

multiply(5,10)

#6

def add(num1, num2, num3, num4):
    print(num1+num2+num3+num4)

add(9,11,9,11)

#7

num_list=[1,2,3,4,5]
def num_list():
    for i in (num_list):
     num_list=num_list+1
     print(num_list)

#8
def min_max_nums(numbers):
    min_num=numbers(0)
    max_nums=numbers(0)

    for num in numbers:
        if num<min_num:
            min_num=num
        if num>max_nums:
            max_nums=num

min_max_nums=[2, 6, 9, 1, 5]