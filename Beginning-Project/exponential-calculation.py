exponent=int(input("Sayının Üssünü Giriniz: "))
base=int(input("Sayının Tabanını Giriniz: "))
result=1
for i in range(1,exponent+1,1):
    result*=base
print(result)