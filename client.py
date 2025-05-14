import json
from urllib.request import urlopen

def fetch_books_data(url):
    try:
        with urlopen(url) as response:
            data = json.loads(response.read().decode())
            print("Books Data Loaded Successfully:\n")
            for book in data:
                print(f"Title: {book['name']}")
                print(f"Description: {book['description']}")
                print("Specifications:")
                for key, value in book['specifications'].items():
                    print(f"  {key}: {value}")
                print(f"Tags: {', '.join(book['tags'])}\n")

            user_input = input("What is the next book you're gonna read ? ").strip().lower()
            found = False
            for book in data:
                if book['name'].strip().lower() == user_input:
                    print("\n📘 Here are informations about your next book :")
                    print(f"Title: {book['name']}")
                    print(f"Description: {book['description']}")
                    print("Specifications:")
                    for key, value in book['specifications'].items():
                        print(f"  {key}: {value}")
                    print(f"Tags: {', '.join(book['tags'])}")
                    found = True
                    break
            if not found:
                print("\n Sorry, we know nothing about this book.")
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    url = "https://jessicajnx.github.io/digital_ecosistem/custom_data.json"
    fetch_books_data(url)
