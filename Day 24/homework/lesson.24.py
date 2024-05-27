#1
def num_list(list):
    for i in list:
        if i==int or i==str or i==float:
            return sum(list)
print(num_list([1,2,3,2.3,"mari"]))

#2
def num_list(numbers):
    return int(sum(numbers))
print(num_list([1,2,3.4,1]))

#3
def num_list(numbers):
    result=0
    for x in numbers:
        if x%x==0:
            result=result+x
            return result
print(num_list([4]))

#4
word=input("enter your word: ")

for i in word:
    if i==i.upper():
        word=word+(i.lower())
    elif i==i.lower():
       word=word+(i.upper())
print(word)

#5
def manual_count(num,count_num):
    num_count=0
    for i in num:
        num_count=num.count(count_num)
    return(num_count)
num=[4,5,5,5,6,5]
print(manual_count(num,5))