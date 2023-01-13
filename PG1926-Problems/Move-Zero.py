numbers = []

number = input("Bir sayı listesi girin: ")

numbers.append(number)

sortnumber = numbers.sort() #küçükten büyüğe sıralama
rsortnumber = number.sort(reverse=True) #büyükten küçüğe sıralam

def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
            if min_index != i:
                
print(numbers)
print(sortnumber)
