import connect
from models import Author, Quote
from cache import get_cache, set_cache


def search_by_author(name):
    key = f"author:{name.lower()}"

    cached_quotes = get_cache(key)

    if cached_quotes:
        print("Result from cache:")
        print(cached_quotes)
        return

    author = Author.objects(fullname__icontains=name).first()

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

    quotes = Quote.objects(tags__icontains=tag)

    if not quotes:
        print("No quotes found")
        return

    result = "\n".join(quote.quote for quote in quotes)

    set_cache(key, result)

    print("Result from MongoDB:")
    print(result)


def search_by_tags(tags):
    tags = [tag.strip().lower() for tag in tags]
    key = f"tags:{','.join(sorted(tags))}"

    cached_quotes = get_cache(key)

    if cached_quotes:
        print("Result from cache:")
        print(cached_quotes)
        return

    quotes = Quote.objects(tags__in=tags)

    if not quotes:
        print("No quotes found")
        return

    result = "\n".join(quote.quote for quote in quotes)

    set_cache(key, result)

    print("Result from MongoDB:")
    print(result)


while True:
    choice = input("Enter command (author, tag, tags, exit): ")

    if choice == "exit":
        print("Goodbye!")
        break

    elif choice == "author":
        name = input("Enter author name: ")
        search_by_author(name)

    elif choice == "tag":
        tag = input("Enter tag: ")
        search_by_tag(tag)

    elif choice == "tags":
        tags = input("Enter tags separated by comma: ").split(",")
        tags = [tag.strip() for tag in tags]
        search_by_tags(tags)

    else:
        print("Unknown command")
