🎬 Movie Recommendation System (ML + Web App)
📌 Project Overview

The Movie Recommendation System is a machine learning–based web application that suggests movies to users based on their input.
It uses content-based filtering to recommend movies that are similar in genre, storyline, keywords, cast, and crew.

The project is built using:

Machine Learning (Python)

Flask Backend API

HTML, CSS, JavaScript Frontend

🎯 Objectives

To recommend similar movies based on user input

To understand content-based recommendation systems

To integrate ML models with a web application

To build a full-stack ML project suitable for real-world use

🛠️ Technologies Used
🔹 Backend & ML

Python

Pandas

NumPy

Scikit-learn

Flask

Flask-CORS

🔹 Frontend

HTML

CSS

JavaScript

📂 Project Structure
movie_recommender/
│
├── dataset/
│   └── movies.csv          # Training dataset (200 movies)
│
├── frontend/
│   ├── index.html          # UI
│   ├── style.css           # Styling
│   └── script.js           # API calls
│
├── model.py                # ML model training
├── app.py                  # CLI testing
├── api.py                  # Flask REST API
├── movies.pkl              # Trained movie data
├── similarity.pkl          # Cosine similarity matrix
├── requirements.txt        # Required libraries
└── README.md               # Project documentation

📊 Dataset Description

The dataset contains 200 movies from different genres:

Action

Comedy

Drama

Sci-Fi

Horror

Romance

Thriller

Each movie includes:

title, genres, overview, keywords, cast, crew

🧠 Methodology
1️⃣ Data Preprocessing

Missing values are handled

Important features are combined into a single text column (tags)

Text data is converted to lowercase

2️⃣ Feature Extraction

CountVectorizer is used to convert text into numerical vectors

3️⃣ Similarity Calculation

Cosine Similarity is applied to find similarity between movies

4️⃣ Recommendation Logic

User input is matched using case-insensitive and partial matching

Top 5 most similar movies are recommended

🖥️ How to Run the Project
🔹 Step 1: Install Dependencies
python -m pip install -r requirements.txt

🔹 Step 2: Train the Model
python model.py


This generates:

movies.pkl

similarity.pkl

🔹 Step 3: Start Backend API
python api.py


Backend runs at:

http://127.0.0.1:5000

🔹 Step 4: Run Frontend

Open frontend/index.html using Live Server in VS Code

Enter a movie name (e.g., Die Hard, Joker)

Click Recommend

✅ Sample Output
Input Movie: Die Hard

Recommended Movies:
- Gladiator
- The Dark Knight
- John Wick
- Mad Max Fury Road
- Inception

📈 Advantages

Simple and fast recommendation

No user login required

Easy to understand and explain

Suitable for academic projects

⚠️ Limitations

Depends on available movie metadata

Does not consider user ratings

Content-based only (no collaborative filtering)

🚀 Future Enhancements

Add movie posters using TMDB API

Implement autocomplete for movie names

Add collaborative filtering

Deploy application online

Improve UI with dark/neon themes

🎓 Academic Use

This project is developed for learning and academic purposes to understand:

Machine Learning

Recommendation Systems

Full-stack integration

👨‍💻 Developed By

Karthik
2nd Year Engineering Student
Movie Recommendation System Project
