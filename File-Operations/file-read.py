file=open("numbers.txt","r")
content=file.read()
file.close()
for i in content.splitlines():
    print(i)