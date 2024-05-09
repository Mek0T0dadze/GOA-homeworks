#1
#შმოტანილი 5 ბოსტნეულის სახეობიდან დაბეჭდეთ მესამე ბოსტნეულამდე
 
vegetables=("carrot", "cucumber", "broccoli", "potato", "tomato")
for i in vegetables:
    print(i)
    if i=="broccoli":
        break

#2
#მომხმარებელს შემოატანინეთ რიცხვი და დაუბეწდეთ ამ კონკრეტულ რიცხვამდე.

num=int(input("enter num: "))
for i in range(0,num+1):
    print(i)

#3
#მომხმარებელს შემოატანინეთ რიცხვი და თუ რიცხვი 50-ზე მეტი იქნება 50-ს აღარ დაუპრინტოთ

num=int(input("enter num: "))

for i in (0,num+1):
    if num==50:
        break

#4
#მომხმარებელს კითხეთ 3 ფერი და 3 საგანი რადგან მერე დაუბეჭდოთ ისინი მათ
user_color=str(input("enter 3 coolors (dont forget to use strings):"))
user_thing=str(input("enter 3 things (dont forget to use strings): "))
for i in user_color:
    for x in user_thing:
        print(i,x)


#5
#მომხმარებელმა შემოიტანა რიცხვი და თუ მის რიცხვში 20 შედის გამოტოვეთ 20 რადგან მომხმარებელს რიცხვი 20 არ მოწონს
num=100
for i in (0,num+1):
    if i==20:
        continue
    print(i)