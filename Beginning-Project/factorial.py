number=int(input("Enter the factorial number: "))
factorial=1
counter=1
while number+1 > counter:
    factorial*=counter
    counter+=1
print(factorial)