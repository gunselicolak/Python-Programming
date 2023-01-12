number = int(input("@ işaretinden sonra mail adresinizin uzunluğu nedir: "))
mail = input("Mail Adresinizi Girin: ")

def control(mail):
    count = 0
    while count == number:
        for ch in mail:
            if ch == '@':
                count = count + 1
                break
            if ch == ".":
                conut = count + 1
                break

    if count == number:
        return True
    else:
        return False

if(control(mail) == True):
    print('Mail adresiniz doğrudur.')
else: 
    print('Mail adresiniz yanlıştır.')