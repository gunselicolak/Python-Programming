import requests
file=open("fuzzing.txt", "r")
content=file.read()
file.close()
header={"Cookie: " "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bdd94"}
for i in content.split("\n"):
    print(i)
    url="https://10.10.10.10" +str(i)
    result=requests.get(url=url, headers=header)
    if "200" in str(result.status_code):
        print("Dosya veyda dizin var: ", i)
    else:
        print("Dosya veya dizin yok: ", i)