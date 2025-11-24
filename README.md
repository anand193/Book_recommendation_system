📚 Book Recommendation System (Streamlit App)

---
![Project Logo](https://img.shields.io/badge/Streamlit-Deployed-green)
**Deployed Application:** [Visit the App](https://bookrecommendationsystem-3fu7yuasc6ruhetqehxaid.streamlit.app/)

A Collaborative Filtering–based Book Recommendation System built using K-Nearest Neighbors (KNN) and deployed through an interactive Streamlit web application. This project recommends similar books based on user reading patterns and rating behavior, using item-based filtering techniques.

🚀 Overview

This project uses item-based collaborative filtering, where books are represented as vectors based on user ratings. Using the cosine similarity metric, the KNN model identifies books that are closely related to the selected title. The system is lightweight, fast, and fully interactive through Streamlit.

---
✨ Key Features

Interactive Streamlit UI
Select books from a dropdown and generate recommendations instantly.

Collaborative Filtering (Item-Based)
Recommendations are based purely on user–book interaction data.

KNN Algorithm with Cosine Similarity
Efficiently finds the nearest neighboring books using sparse vector similarity.

Minimal Dependencies
Runs smoothly using common Python data science libraries.

⚙️ Prerequisites

Ensure you have:

Python 3.x

The following files placed in the same directory as app.py:

book_pivot1.pkl — Contains the index of all book titles.

book_sparse.npz — Contains the sparse user–book rating matrix.

Install required packages:

pip install pandas numpy scikit-learn scipy streamlit

💻 Installation & Setup

Clone the repository or copy the project folder.

Place the following files in the project directory:

app.py

book_pivot1.pkl

book_sparse.npz

Install the dependencies.

Launch the Streamlit app:

streamlit run app.py


Your browser will open automatically at:

http://localhost:8501

🧑‍💻 How to Use the Application

Select a Book from the dropdown list.

Click Recommend.

The system displays the top 5 most similar books based on collaborative filtering.

🧠 Model Details
🔍 Algorithm

The recommendation engine is built using:

scikit-learn’s NearestNeighbors

Cosine Similarity as the distance metric
(Similarity = 1 – distance)

📊 Data

Rows: Book titles

Columns: User IDs

Values: Ratings

Format: CSR sparse matrix

⚡ Core Logic

Load:

book_pivot1.pkl → DataFrame of book titles

book_sparse.npz → Sparse rating matrix

Initialize and train a KNN model:

model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(book_sparse_matrix)


Recommendation Function:

Find index of selected book using np.where

Retrieve nearest neighbors using model.kneighbors()

Return top 5 recommended titles
