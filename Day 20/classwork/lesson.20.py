#1
int_list=[1,2,3,4,5,6,7,8,9,10]
even_list=[]
for i in int_list:
    if i%2==0:
        even_list.append(i)
print(even_list)

#2
num_list=[1,2,3,4,5]
for i in num_list:
    if num_list!=0:
        index=num_list.index(i)
        num_list.pop(index)
print(num_list)
