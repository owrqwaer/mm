import requests
from bs4 import BeautifulSoup
import lxml

url = "https://rozetka.com.ua/tablets/c130309/"
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
headers = {"User-agent": user}

session = requests.Session()

response = session.get(url, headers = headers)
#print(response.status_code)

if response.status_code == 200:
    all_products = soup.find_all('li', class_="ng-star-inserted")
    soup = BeautifulSoup(response.text, "lxml")
    all_products = soup.find("li", class_ ="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted"):
    for i in all_products:
    try:
        temp = i.find('div', class_= 'goods-tile__price--old price--gray ng-star-inserted')
        price =i.find('span', class_="good-tile__price-value")
        print(price.text)
        print(temp)
    except ValueError:

        print('Знижки немає')

print(all_products.text)

