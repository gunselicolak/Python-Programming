transaction= input('Enter Transaction: ')
number1=int(input('Number One: '))
number2=int(input('Number Two: '))
if transaction=="+":
    result=int(number1)+int(number2)
    print("Result: ", str(result))
elif transaction=="-":
    result=int(number1)-int(number2)
    print("Result: ", str(result))
elif transaction=="*":
    result=int(number1)*int(number2)
    print("Result: ", str(result))
elif transaction=="/":
    result=int(number1)/int(number2)
    print("Result: ", str(result))