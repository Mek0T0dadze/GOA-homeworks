
#1
def initial_charts(splited_fullname):
    splited_fullname=splited_fullname.split(" ")
    firstname=splited_fullname[0]
    lastname=splited_fullname[1]
result="firstname[]"+"."+"lastname[0]"

print(result)

initial_charts=("Meko Todadze")

#2
def list(numbers):
    jami=sum(numbers)
    result=jami//len(numbers)
    print(result)

list([1,2,3,4,5])

#3
def is_palidrom(word):
    reversed_word=''
    for i in range(len(word)-1,-1,-1):
        reversed_word=reversed_word+word(i)
    print(reversed_word)

is_polidrom=("Meko")
#4
def remove_space(word):
    removed_space=""

    for i in word:
        if i!=" ":
            removed_space=removed_space+i
    print(removed_space)

remove_space("Meko Todadze")


#5
def num_list(numbers):
    sum=0
    quantity=0

    for i in numbers:
        if i<0:
            quantity=quantity+i
        else:
            sum=sum+1
    print(sum,quantity)
num_list([1,2,-3,-4])