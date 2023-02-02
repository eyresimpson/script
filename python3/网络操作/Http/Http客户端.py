import requests

url = "http://www.baidu.com"

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print("Failed to get response from server, status code:", response.status_code)
