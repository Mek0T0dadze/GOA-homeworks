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
#5
def count_by(x, n):
    for i in range(x,n+1):
        return i
print(count_by(1,10))

#6
#7
#8
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
