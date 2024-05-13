#1
def num(numbers):
    return [4,5,6]
print(num)

def say_hello(name):
    return ("hello(name)")
print(say_hello)

def fruits(fruit1,fruit2):
    return fruit1,fruit2
fruits("cherry","strawberry")
print(fruits("cherry","strawberry"))

def code_leng(word1,word2):
    return word1,word2
code_leng("python", "js")
print(code_leng("python","js"))

def names(name1,name2):
    return name1,name2
names("Meko","Mari")
print(names("Meko","Mari"))
#2
def num_list(numbers):
    even_num=0
    for i in numbers:
        if i==numbers[2]and numbers[4]:
            even_num=even_num+3+5
            return even_num
num_list([1,2,3,4,5])
print(num_list([1,2,3,4,5]))

#3
def num_list(numbers):
    odd_result=0
    even_result=0
    for i in numbers:
        if i%2==0:
            even_result=even_result+i
        else:
            odd_result=odd_result+i
    return odd_result,even_result
print(num_list([1,2,3,4,5]))
#4
def num_list(numbers):
    quality=0
    for i in numbers:
        quality=quality+len(numbers)
    return quality
print(num_list([1,2,3,4,5]))

#5
def num_list(numbers):
    for i in numbers:
        if numbers[2]==3:
            numbers[2]==2
    num_list([1,2,3,4,5])
print(num_list)

#6
def names(name):
    if name ==("Meko"):
        name=name+("Todadze")
    names=("Meko")
print(names)