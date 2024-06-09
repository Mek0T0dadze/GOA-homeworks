def manual_pop(numbers,index_to_pop):
    result=[]
    for index in range(len(numbers)):
        if index != index_to_pop:
            result.append(numbers[index])
        return result
print(manual_pop([1,2,3],[2]))