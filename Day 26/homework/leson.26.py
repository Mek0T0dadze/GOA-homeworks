#1
name=input("enter your name: ")
print(name.capitalize())
print(name.upper())
print(name.lower())

 #2 
def find_index(word, find_char):
     for index in range(len(word)):
          if word[index]==find_char:
               return index
print(find_index("meko","k"))

#3
def manual_len(collection):
     count=0
     for item in collection:
          count=count+1
          return count
print(manual_len(["meko", 1,"true"]))

#4
names=["meko","mari"]
names.insert (1, "babi")
print(names)

numbers=[1,2,3,4,5]
numbers.pop(3)
print(numbers)

numbers=[1,2,3,4,5]
len(numbers)
print(numbers)

numbers=[1,2,3,4,5]
numbers.append(6)
print(numbers)
