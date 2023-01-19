data="Python 101"
beginning=list(data)
print(beginning)
letter_counter=0
number_counter=0
for i in beginning:
    if str(i).isdecimal():
        number_counter+=1
    else:
        letter_counter+=1
print("number of digits: ",number_counter)
print("number of characters: ",letter_counter)