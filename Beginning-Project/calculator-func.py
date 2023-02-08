def calculator(num1, num2, operation):
    if operation=="+":
        result=num1+num2
    elif operation=="-":
        result=num1-num2
    elif operation=="*":
        result=num1*num2
    elif operation=="/":
        result=num1/num2
    else:
        result="Hata"
    return result
print(calculator(10, 2, '*'))