import random
random_number=round(random.random()*100)
print(random_number)
enter_number=int(input("Enter a number between 0-100: "))
while random_number != enter_number:
    if enter_number>=random_number:
        print("You entered a large number!")
    else:
        print("You entered a small number!")
    enter_number=int(input("Enter a number between 0-100: "))
print("Congratulations! You have won the game!!")