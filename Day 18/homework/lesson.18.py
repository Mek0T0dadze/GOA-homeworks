#1
name=input("enter your name: ")
print(name==name.lower())

#2
word=input("enter upercase word: ")
count=1
for char in word:
    if char.lower()in word:
        print("enter upercase word: ")
        count=count+1
print(count,word)
#3
#user_word=input("enter your name: ")
#result=""
#for index in user_word:
 #   if index %2==0:
#        result=result+user_word[index].upper()
 #   else:
  #      result=result+user_word[index].lower()

#print(result)
#4
name="Meko"
if name.index("Meko")==[5]:
    print(name.upper())
elif name.index("Meko")<5:
    print(name.lower())

#5
names=["nika","luka","mari"]
for index in len(names):
    name[index]=name[index].capitalize

print(names)
#6
name=input("enter your name: ").capitalize
surname=input("enter your surname: ").capitalize
result=name[0]+'.'+surname[0]
print(result)

#7
def manual_find(collection,find_manual):
    for index in range(len(collection)):
        if collection[index==find_manual]:
            return[index]
    return -1
print(manual_find("meko","k"))

#8
def manual_word(collection,manual):
    for index in range(len(collection)):
        if collection[index==manual]:
            return[index]
    return -1
print(manual_word("meko","k"))
#9
mom="Mancho"
dad="zura"
sis1="Mari"
sis2="Meko"
sis3="Babi"
join_char="-"
print("mom"+"join_char"+"dad"+"join_char"+"sis1"+"join_char"+"sis2"+"join_char"+"sis3")
#10
string_list=[]
for i in range(5):
    print(input("enter your name:"))
    string_list.appedn(word)

join_char=input("enter witch char you want to join in list: ")
for index in len(string_list):
    if index%2==0:
        result=result+string_list[index]+join_char
    result=result-1
print(result)
#11
name="Meko"
name_info=""
n=name.lower()
a=name.upper()
m=name.capitalize()
e=name.find()
name_info=name_info+"n"+"a"+"m"+"e"
join_char="-".join(name_info)

