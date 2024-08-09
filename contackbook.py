"""contactbook app"""
names=[]
numbers=[]

num = 3

for i in range(num):
    name=input("enter the name")
    number=input("enter the phone number")

    names.append(name)
    numbers.append(number)

print("\tname\t\t\tphone number")

for i in range(num):
    print(f'\t{names[i]}\t\t\t{numbers[i]}')

s=input("enter the name to search")

if s in names:
    index=names.index(s)
    name=names[index]
    number=numbers[index]

    print(f"name: {name},phone number{number}")

else:
    print("name not found")