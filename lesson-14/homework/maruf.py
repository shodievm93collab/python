1. JSON Parsing: Read students.json and print student details

Assuming students.json looks like this:

[
    {"name": "Alice", "age": 22, "major": "Physics"},
    {"name": "Bob", "age": 24, "major": "Mathematics"},
    {"name": "Charlie", "age": 21, "major": "Computer Science"}
]

import json

def parse_students_json(filename='students.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        students = json.load(f)

    for student in students:
        print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

if __name__ == "__main__":
    parse_students_json()

2. Weather API: Fetch weather data for Tashkent
import requests

def fetch_weather(city='Tashkent'):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'  # Replace with your actual API key from https://openweathermap.org/api
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description'].capitalize()}")
        print(f"Wind speed: {data['wind']['speed']} m/s")
    else:
        print(f"Failed to get weather data: {response.status_code} - {response.reason}")

if __name__ == "__main__":
    fetch_weather()


Note: You must sign up at https://openweathermap.org/
 and get an API key, then replace 'YOUR_OPENWEATHERMAP_API_KEY' with it.

3. JSON Modification: Add, update, delete books from books.json

Sample books.json format:

[
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

import json
import os

BOOKS_FILE = 'books.json'

def load_books():
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_books(books):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4)

def add_book():
    books = load_books()
    new_id = max([book['id'] for book in books], default=0) + 1
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    books.append({"id": new_id, "title": title, "author": author})
    save_books(books)
    print("Book added.")

def update_book():
    books = load_books()
    book_id = int(input("Enter book ID to update: "))
    for book in books:
        if book['id'] == book_id:
            title = input(f"Enter new title (leave blank to keep '{book['title']}'): ")
            author = input(f"Enter new author (leave blank to keep '{book['author']}'): ")
            if title:
                book['title'] = title
            if author:
                book['author'] = author
            save_books(books)
            print("Book updated.")
            return
    print("Book not found.")

def delete_book():
    books = load_books()
    book_id = int(input("Enter book ID to delete: "))
    books = [book for book in books if book['id'] != book_id]
    save_books(books)
    print("Book deleted if existed.")

def list_books():
    books = load_books()
    if not books:
        print("No books available.")
    for book in books:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")

def book_manager():
    while True:
        print("\nOptions: list, add, update, delete, exit")
        choice = input("Choose an option: ").lower()
        if choice == 'list':
            list_books()
        elif choice == 'add':
            add_book()
        elif choice == 'update':
            update_book()
        elif choice == 'delete':
            delete_book()
        elif choice == 'exit':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    book_manager()

4. Movie Recommendation System (OMDb API)
import requests
import random

def movie_recommendation():
    api_key = 'YOUR_OMDB_API_KEY'  # Get API key at http://www.omdbapi.com/apikey.aspx
    genre = input("Enter a movie genre (e.g. Action, Comedy): ").strip()

    url = f"http://www.omdbapi.com/?apikey={api_key}&type=movie&s={genre}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get('Response') == 'True':
            movies = data.get('Search', [])
            if movies:
                movie = random.choice(movies)
                print(f"Recommended movie in genre '{genre}':")
                print(f"Title: {movie['Title']}")
                print(f"Year: {movie['Year']}")
                print(f"IMDB ID: {movie['imdbID']}")
                # Optionally, fetch more details
                details_url = f"http://www.omdbapi.com/?apikey={api_key}&i={movie['imdbID']}&plot=short"
                details_resp = requests.get(details_url)
                if details_resp.status_code == 200:
                    details = details_resp.json()
                    print(f"Plot: {details.get('Plot', 'N/A')}")
                    print(f"IMDB Rating: {details.get('imdbRating', 'N/A')}")
            else:
                print("No movies found for that genre.")
        else:
            print(f"API Error: {data.get('Error')}")
    else:
        print(f"Failed to fetch movies: {response.status_code}")

if __name__ == "__main__":
    movie_recommendation()
