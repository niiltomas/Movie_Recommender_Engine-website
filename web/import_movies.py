import json

# Path to your JSON file
JSON_FILE = "movies_weighted.json"

def load_movies():
    """Load movies from the JSON file."""
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("JSON file not found. Starting with an empty list.")
        return []
    except json.JSONDecodeError:
        print("Invalid JSON format. Starting with an empty list.")
        return []

def save_movies(movies):
    """Save movies back to the JSON file."""
    with open(JSON_FILE, "w") as file:
        json.dump(movies, file, indent=4)
    print("Movies saved successfully!")

def calculate_movie_statistics(ratings):
    """Calculate statistics for the movie based on ratings."""
    rating_count = len(ratings)
    movie_average = sum(ratings) / rating_count if rating_count > 0 else 0
    # Example weighted average formula
    
    return movie_average, rating_count

def delete_movie(movies):
    """Delete a movie by its ID."""
    try:
        movie_id = int(input("\nEnter the ID of the movie to delete: "))
        for movie in movies:
            if movie["movie_id"] == movie_id:
                movies.remove(movie)
                print(f"Movie '{movie['title']}' has been deleted successfully!")
                return
        print("Error: No movie found with that ID!")
    except ValueError:
        print("Error: Please enter a valid numeric ID!")


def add_movie(movies):
    """Add a new movie to the list."""
    print("\nAdding a new movie...")

    # Input fields for the movie
    movie_id = int(input("Enter movie ID (unique integer): "))
    if any(movie["movie_id"] == movie_id for movie in movies):
        print("Error: A movie with this ID already exists!")
        return

    title = input("Enter movie title: ")
    genres = input("Enter genres (comma-separated): ").split(",")
    year = int(input("Enter release year: "))
    ratings = list(map(float, input("Enter ratings (comma-separated): ").split(",")))

    # Calculate derived fields
    movie_average, rating_count, weighted_average_adjusted = calculate_movie_statistics(ratings)

    # Create a new movie object
    new_movie = {
        "movie_id": movie_id,
        "title": title,
        "genres_arr": [genre.strip() for genre in genres],
        "ratings_list": ratings,
        "movie_average": movie_average,
        "rating_count": rating_count,
        "year": year,
    
    }

    # Add to the list
    movies.append(new_movie)
    print(f"Movie '{title}' added successfully!")

def main():
    """Main function to manage the JSON data."""
    movies = load_movies()

    while True:
        print("\nMovie Manager")
        print("1. View movies")
        print("2. Add a new movie")
        print("3. Delete a movie")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            for movie in movies:
                print(f"{movie['movie_id']} - {movie['title']} ({movie['year']})")
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            delete_movie(movies)
        elif choice == "4":
            save_movies(movies)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()