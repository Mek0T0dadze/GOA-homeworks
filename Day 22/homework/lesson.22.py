#1
#def manual_pop(list,list_index):
    #new_colection=[]
    #for index in range(0,len(list)):
        #if index!=list_index:
            #new_colection=new_colection.append(list[index])
        #return new_colection
#names=["meko","babi","mari"]
#print(manual_pop(names,2))

#2

def manual_count(num,count_num):
    num_count=0
    for i in num:
        num_count=num.count(count_num)
    return(num_count)
num=[1,2,3,4,5,4]
print(manual_count(num,4))

def maual_count(numbers,count_num):
    result=0
    num_count=0
    for i in  numbers:
        result=sum(numbers)//len(numbers)
        num_count=result.count(count_num)
    return result,num_count
numbers=[5,2,3,10]
print(manual_count(numbers,4))
#3
def manual_min(numbers):
    miniest_num=[]
    for i in numbers:
        if i<numbers:
            miniest_num=miniest_num+numbers
    return miniest_num
print(manual_min([4,6,3,7]))

def manual_min(numbers):
    miniest_num=[]
    for i in numbers:
        if i<numbers:
            miniest_num=miniest_num+numbers
    return miniest_num
print(manual_min([1,2,3,4,5,6,7,8,9,10]))
