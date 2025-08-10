import json


with open("students.json", "r", encoding="utf-8") as file:
    data = json.load(file)  

for student in data.get("students", []):  
    print("Name:", student.get("name"))
    print("Age:", student.get("age"))
    print("Grade:", student.get("grade"))
    print("-" * 30)


{
    "students": [
        {"name": "Alice", "age": 20, "grade": "A"},
        {"name": "Bob", "age": 22, "grade": "B"},
        {"name": "Charlie", "age": 21, "grade": "A"}
    ]
}



import requests

API_KEY = "Dil_API_key"  
CITY = "Tashkent"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL)
    response.raise_for_status()  

    data = response.json()

    
    city_name = data["name"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description.capitalize()}")

except requests.exceptions.RequestException as e:
    print("Error fetching weather data:", e)




{
    "books": [
        {"id": 1, "title": "1984", "author": "George Orwell"},
        {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
    ]
}



import json
import os

FILENAME = "books.json"


def load_books():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return {"books": []}


def save_books(data):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def add_book():
    data = load_books()
    new_id = max([book["id"] for book in data["books"]], default=0) + 1
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    data["books"].append({"id": new_id, "title": title, "author": author})
    save_books(data)
    print("✅ Book added successfully.")


def update_book():
    data = load_books()
    book_id = int(input("Enter book ID to update: "))
    for book in data["books"]:
        if book["id"] == book_id:
            book["title"] = input(f"Enter new title (current: {book['title']}): ") or book["title"]
            book["author"] = input(f"Enter new author (current: {book['author']}): ") or book["author"]
            save_books(data)
            print("✅ Book updated successfully.")
            return
    print("❌ Book not found.")


def delete_book():
    data = load_books()
    book_id = int(input("Enter book ID to delete: "))
    data["books"] = [book for book in data["books"] if book["id"] != book_id]
    save_books(data)
    print("✅ Book deleted successfully.")


def main():
    while True:
        print("\n📚 Book Manager")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()





import requests
import random

API_KEY = "DIL_API_key"  
BASE_URL = "http://www.omdbapi.com/"

def search_movies_by_genre(genre):
    
    keywords = ["love", "war", "space", "adventure", "crime", "horror", "comedy", "action"]
    keyword = random.choice(keywords)  

    params = {
        "apikey": API_KEY,
        "s": keyword,
        "type": "movie",
        "page": random.randint(1, 5)  
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Search" not in data:
        return []

    movies = []
    for movie in data["Search"]:
        details = requests.get(BASE_URL, params={"apikey": API_KEY, "i": movie["imdbID"]}).json()
        if "Genre" in details and genre.lower() in details["Genre"].lower():
            movies.append(details)

    return movies

def recommend_movie():
    genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ").strip()
    movies = search_movies_by_genre(genre)

    if not movies:
        print(f"❌ No movies found for genre: {genre}")
        return

    movie = random.choice(movies)
    print("\n🎬 Recommended Movie:")
    print(f"Title: {movie['Title']}")
    print(f"Year: {movie['Year']}")
    print(f"Genre: {movie['Genre']}")
    print(f"Plot: {movie['Plot']}")
    print(f"IMDB Rating: {movie['imdbRating']}")

if __name__ == "__main__":
    recommend_movie()
