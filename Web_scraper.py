import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com"
response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")
print(len(books))

for book in books:
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").text.encode("latin-1").decode("utf-8")
    print(title, price)

with open("books.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text.encode("latin-1").decode("utf-8")
        writer.writerow([title, price])

print("Done! Check books.csv")
