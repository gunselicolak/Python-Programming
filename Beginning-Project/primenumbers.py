number = int(input("Specify up to which number to print prime numbers: "))
print(2)
for i in range(3,number,1):
    control=False
    for j in range(2,i):
        if i%j==0:
            control=True
    if control==False:
        print(i)