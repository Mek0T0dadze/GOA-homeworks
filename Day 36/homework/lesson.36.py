person1={
    'name':'Meko',
    'surname':'Todadze',
    'age':'14'
}

person2={
    'name':'Mari',
    'surname':'Todadze',
    'age':'15'
}

person3={
    'name':'barbare',
    'surname':'Todadze',
    'age':'7'
}

person4={
    'name':'keta',
    'surname':'ashadze',
    'age':'14'
}

people = ""
for person in [person1, person2, person3, person4]:
    people += f"{person['name']} {person['surname']} {person['age']} " 
print(people)