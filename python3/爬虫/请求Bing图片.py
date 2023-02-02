import requests
import os

url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"

response = requests.get(url)
data = response.json()
img_url = "https://www.bing.com" + data["images"][0]["url"]
img_response = requests.get(img_url)

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
img_path = os.path.join(desktop, "bing_image.jpg")

with open(img_path, "wb") as f:
    f.write(img_response.content)

print("图片已保存到桌面！" + desktop)
