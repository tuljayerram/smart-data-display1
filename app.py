from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def show_books():
    query = "bestsellers"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=20"

    response = requests.get(url)
    data = response.json()

    books = []
    for item in data.get("items", []):
        info = item.get("volumeInfo", {})
        book = {
            "title": info.get("title", "No Title"),
            "description": info.get("description", "No description available."),
            "link": info.get("infoLink", "#")
        }
        books.append(book)

    return render_template("index.html", books=books)

if __name__ == '__main__':
    app.run(debug=True)