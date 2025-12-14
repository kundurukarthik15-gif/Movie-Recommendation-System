import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# Load dataset (correct path)
movies = pd.read_csv(os.path.join("dataset", "movies.csv"))

# Select required columns
movies = movies[['title', 'genres', 'overview', 'keywords', 'cast', 'crew']]

# Fill missing values
movies.fillna('', inplace=True)

# Combine features
movies['tags'] = (
    movies['genres'] + ' ' +
    movies['overview'] + ' ' +
    movies['keywords'] + ' ' +
    movies['cast'] + ' ' +
    movies['crew']
)

# Keep required columns
movies = movies[['title', 'tags']]

# Convert to lowercase
movies['tags'] = movies['tags'].apply(lambda x: x.lower())

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Similarity calculation
similarity = cosine_similarity(vectors)

# Save model files
pickle.dump(movies, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ Model trained successfully")
