#1
def num_list(numbers):
    result=0
    for i in numbers:
        if i % 2 ==0 or i % 2 ==0.5:
            i * 2
        else:
            i * 4
            result=result+i
            return result
print(num_list([2,3,2.3]))

#2
def str_list(collection):
    result=""
    for index in range(len(collection)):
        if index%2==0:
            result=index.upper()
        else:
            result=index.lower()
            return result
print(str_list("meko"))

#3
def to_jaden_case(string):
    string = string.split()
    result=[]
    for i in string:
        result.append(i.capitalize())
    return " ".join(result)
print(to_jaden_case("hello this is goa"))
#7
def colection(list,str_to_find):
    result=[]
    for i in list:
        if str_to_find==i in list:
            result=result+str_to_find
    return result
print(colection(["meko"],["e"]))       

#8
def num_list(numbers):
    result=0
    for num in numbers:
        if num%2!=0:
            result==result+num
        else:
            pass
        return result
print(num_list([1,2,3,4]))

#9
def sentence_lists(sentence1, sentence2):
    sentence_listst = sentence1 + sentence2
    return sentence_lists
print(sentence_lists("hello my name is meko","i am 14 yo"))
