def even_numbers(number):
    list=[]
    for i in range(1,number,1):
        if i%2==0:
            list.append(i)
    return list
print(even_numbers(100))