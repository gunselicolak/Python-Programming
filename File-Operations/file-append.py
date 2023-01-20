for i in range(1,100,2):
    file=open("numbers.txt", "a")
    data=str(i)+"\n"
    file.write(data)
    file.close()