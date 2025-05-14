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
    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    url = "https://github.com/jessicajnx/digital_ecosistem.git/custom_data.json/custom_data.json"
    fetch_books_data(url)
