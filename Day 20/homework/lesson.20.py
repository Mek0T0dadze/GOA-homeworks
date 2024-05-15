#1
num_list=[1,2,3,4,5]
result=0
result=result+sum(num_list)//len(num_list)
print(result)

#2

num_list=[1,5,8,-3,-4,-2]
negative_num=0
normal_num=0
for i in num_list:
    if i <0:
        negative_num=negative_num+i
    else:
        normal_num=normal_num+i
    print(negative_num,normal_num)