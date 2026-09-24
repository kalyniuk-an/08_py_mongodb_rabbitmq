import json

from connect import connect
from models import Author, Quote


with open("authors.json", "r", encoding="utf-8") as file:
    authors = json.load(file)

with open("qoutes.json", "r", encoding="utf-8") as file:
    quotes = json.load(file)

print(f"Authors: {len(authors)}")
print(f"Quotes: {len(quotes)}")

for author_data in authors:
    author = Author(
        fullname=author_data["fullname"],
        born_date=author_data["born_date"],
        born_location=author_data["born_location"],
        description=author_data["description"],
    )
    author.save()

print("Autor saved!")

for quote_data in quotes:
    author = Author.objects(fullname=quote_data["author"]).first()

    quote = Quote(
        tags=quote_data["tags"],
        author=author,
        quote=quote_data["quote"],
    )

    quote.save()

print("Quotes saved!")
