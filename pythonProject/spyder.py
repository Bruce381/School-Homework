import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"
}

url = "https://github.com/"

response = requests.get(url, headers=headers)
print(response)
#print(response.text)


'''
#print(response.text)
content = response.text
soup =  BeautifulSoup(content,"html.parser")
all_price = soup.find_all("p",attrs={"class":"price_color"})

for i in all_price:
    print(i.string[1:])
'''



