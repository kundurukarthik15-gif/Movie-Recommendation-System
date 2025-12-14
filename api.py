from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)   # 🔥 THIS LINE IS IMPORTANT

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies = pickle.load(open(os.path.join(BASE_DIR, 'movies.pkl'), 'rb'))
similarity = pickle.load(open(os.path.join(BASE_DIR, 'similarity.pkl'), 'rb'))

def recommend(movie_name):
    index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies['title'].tolist())

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    data = request.json
    movie = data.get('movie')
    recs = recommend(movie)
    return jsonify(recs)

if __name__ == '__main__':
    app.run(debug=True)
