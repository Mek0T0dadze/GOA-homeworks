#1
def litres(time):
    return 0.5*time
print(litres(3))

#2
def blank_pages(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m
print(blank_pages(5, 5))
print(blank_pages(-5, 5))

#3
def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result
print([1,2,3,])
print([4,1,1,1,4])
print([2,2,2,2,2,2])

#4
def fake_bin(x):
    result=" "
    for i in x:
        if int(i) < 5:
            result += "0"
        else:
            result += "1"
    return result
print(fake_bin("45385593107843568"))
#5
def count_by(x, n):
    for i in range(x,n+1):
        return i
print(count_by(1,10))

#6
def to_jaden_case(string):
    string = string.split()
    myarr=[]
    for i in string:
        myarr.append(i.capitalize())
    return " ".join(myarr)
#7
def accum(st):
    result=[]
    for i, char in enumerate(st):
        subtr = char.upper() + char.lower()* i
        result.append(subtr)
    return "-".join(result)
print(accum("abcd"))

#8
def remove_smallest(numbers):
    if not numbers:
        return []
    else:
        nums=numbers.copy
        nums.remove(min(numbers))
    return nums
print(remove_smallest[1,2,3,4,5])

#9
def num_multiples(n):
    if n < 0:
        return 0

    sum_multiples = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
    
    return sum_multiples

print(num_multiples(3))  
print(num_multiples(5)) 
#10
def likes(names):
    names=["peter","jacob","alex","max","john","mark"]
    for i in names:
        if names==[]:
            print("no on likes it")
        elif names==["peter"]:
            print("peter likes it")
        elif names==("jacob","alex"):
            print("jacob and alex likes it")
        elif names==("max","john","mark"):
            print("max,john and mark likes it")
        elif names==("Alex", "Jacob", "Mark", "Max"):
            print("alex,jacob,mark ad max likes it")

