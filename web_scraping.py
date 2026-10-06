import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.find_all("article", class_="product_pod"):

    title = book.h3.a["title"]

    price = book.find("p", class_="price_color").text.strip().replace("Â", "")
    rating = book.p["class"][1]

    availability = book.find(
        "p", class_="instock availability"
    ).text.strip()

    books.append({
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability
    })

df = pd.DataFrame(books)

print(df.head())

df.to_csv("books_data.csv", index=False, encoding="utf-8-sig")

print("Scraping completed successfully!")
print("Total books:", len(df))

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nDataset Shape:")
print(df.shape)
