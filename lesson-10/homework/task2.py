import requests
import random

API_KEY = "abc577e3b07a1b3471d4bfde0badca64"
BASE_URL = "https://api.themoviedb.org/3"

# Get all available genres
def get_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        genres = response.json()["genres"]
        return {genre["name"].lower(): genre["id"] for genre in genres}
    else:
        print("Failed to get genres.")
        return {}

# Get a random movie by genre ID
def get_random_movie(genre_id):
    discover_url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
    response = requests.get(discover_url)
    if response.status_code == 200:
        movies = response.json().get("results", [])
        if not movies:
            print("No movies found for this genre.")
            return None
        return random.choice(movies)
    else:
        print("Failed to get movies.")
        return None

def main():
    genres = get_genres()
    if not genres:
        return

    print("Available genres:")
    for name in genres:
        print(f"- {name.capitalize()}")

    user_genre = input("Enter a genre: ").strip().lower()
    if user_genre not in genres:
        print("Genre not found.")
        return

    movie = get_random_movie(genres[user_genre])
    if movie:
        print(f"\n🎬 Recommended Movie: {movie['title']}")
        print(f"📅 Release Date: {movie.get('release_date', 'Unknown')}")
        print(f"⭐ Rating: {movie.get('vote_average', 'N/A')}")
        print(f"\n📝 Overview:\n{movie.get('overview', 'No description available.')}")

if __name__ == "__main__":
    main()
