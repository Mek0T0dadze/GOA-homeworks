#1
def manual_pop(string, deleted_index):
    new_colection=[]
    for index in range(0,len(string)):
        if index!=deleted_index:
            new_colection.append(string[index])
        return new_colection
names=["meko","mari","babii"]
print (manual_pop(names,0))

#2
def manual_count(colection,item_to_count):
    count=0
    for item in colection:
        if item==item_to_count:
            count=count+1
    return count
names["meko","mari","babi"]
print(manual_count(names,"babi"))