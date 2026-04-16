# Empty list to store movie dictionaries
movies = []

# Collect details for 3 movies
for i in range(3):
    print(f"\nEnter details for Movie {i+1}:")
    title = input("Title: ")
    director = input("Director: ")
    year = input("Release Year: ")
    rating = input("Rating: ")
    
    # Store in dictionary
    movie = {
        "Title": title,
        "Director": director,
        "Year": year,
        "Rating": rating
    }
    movies.append(movie)

# Display movie details
print("\nMovie Details:")
for idx, movie in enumerate(movies, start=1):
    print(f"\nMovie {idx}:")
    for key, value in movie.items():
        print(f"{key}: {value}")