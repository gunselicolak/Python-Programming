for i in range(1,101,1):
    control=False
    if i%3==0:
        control=True
        print("Fizz",end=",")
    if i%5==0:
        control=True
        print("Buzz",end=",")
    if i%3==0 and i%5==0:
        control=True
        print("FizzBuzz",end=",")
    if control==False:
        print(i,end=",")