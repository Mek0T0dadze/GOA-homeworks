#1
def get_count(sentence):
    listn=["a","e","i","o","u"]
    result=0
    for i in listn:
        for j in sentence:
            if i.lower()==sentence.lower():
                result+=result+1
    return result
#2
def square_digits(num):
    to_return=""
    for element in str(num):
        to_return+=to_return+f'{int(element)*int(element)}'
    return int(to_return)
    