list1 = []
list2 = []

numbers = input("Liste: ")

list1.append(numbers)

for num in list1:
    if int(num)%2!=0:
        list2.append(num)

en_büyük = list2[0]
for i in list2:
    if en_büyük < i:
        print(i)
