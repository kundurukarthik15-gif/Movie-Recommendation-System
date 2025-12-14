import pickle

# Load saved files
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_name):
    if movie_name not in movies['title'].values:
        return ["Movie not found in database"]

    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []
    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations


# Test the system
if __name__ == "__main__":
    movie = input("Enter movie name: ")
    results = recommend(movie)

    print("\nRecommended Movies:")
    for r in results:
        print("-", r)

def recommend(movie_name):
    movie_name = movie_name.lower().strip()

    # find matching movie (partial + case-insensitive)
    matches = movies[movies['title'].str.lower().str.contains(movie_name)]

    if matches.empty:
        return ["Movie not found in database"]

    index = matches.index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]
