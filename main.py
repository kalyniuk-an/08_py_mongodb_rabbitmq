import re

import connect
from models import Author, Quote
from cache import get_cache, set_cache


def search_by_name(name):
    key = f"name:{name.lower()}"

    cached_quotes = get_cache(key)

    if cached_quotes:
        print("Result from cache:")
        print(cached_quotes)
        return

    pattern = re.compile(re.escape(name), re.IGNORECASE)

    author = Author.objects(fullname=pattern).first()

    if not author:
        print("Author not found")
        return

    quotes = Quote.objects(author=author)

    result = "\n".join(quote.quote for quote in quotes)

    set_cache(key, result)

    print("Result from MongoDB:")
    print(result)


def search_by_tag(tag):
    key = f"tag:{tag.lower()}"

    cached_quotes = get_cache(key)

    if cached_quotes:
        print("Result from cache:")
        print(cached_quotes)
        return

    pattern = re.compile(re.escape(tag), re.IGNORECASE)

    quotes = Quote.objects(tags=pattern)

    if not quotes:
        print("No quotes found")
        return

    result = "\n".join(quote.quote for quote in quotes)

    set_cache(key, result)

    print("Result from MongoDB:")
    print(result)


def search_by_tags(tags):
    tags = [tag.strip().lower() for tag in tags]

    quotes = Quote.objects(tags__in=tags)

    if not quotes:
        print("No quotes found")
        return

    result = "\n".join(quote.quote for quote in quotes)

    print("Result from MongoDB:")
    print(result)


while True:
    command = input("Enter command: ").strip()

    if command == "exit":
        print("Goodbye!")
        break

    if ":" not in command:
        print("Invalid command")
        continue

    command_name, value = command.split(":", 1)

    command_name = command_name.strip().lower()
    value = value.strip()

    if command_name == "name":
        search_by_name(value)

    elif command_name == "tag":
        search_by_tag(value)

    elif command_name == "tags":
        tags = value.split(",")
        search_by_tags(tags)

    else:
        print("Unknown command")
