import streamlit as st
import numpy as np
import pickle
from scipy.sparse import load_npz
from sklearn.neighbors import NearestNeighbors

# -----------------------------------
# Load Data
# -----------------------------------
st.title("📚 Book Recommendation System")

# Load pivot table (index = book titles)
book_pivot = pickle.load(open("book_pivot1.pkl", "rb"))
book_titles = book_pivot.index.tolist()

# Load sparse matrix
book_sparse = load_npz("book_sparse.npz")

# -----------------------------------
# Train NearestNeighbors model
# (must be recreated because model was not saved)
# -----------------------------------
model = NearestNeighbors(metric='cosine', algorithm='brute', n_jobs=1)
model.fit(book_sparse)

# -----------------------------------
# Recommendation function
# -----------------------------------
def recommend_book(book_name, model, data, n_neighbors=6):
    # get index of selected book
    book_index = np.where(book_pivot.index == book_name)[0][0]

    # query kneighbors
    query = data[book_index].reshape(1, -1)
    distances, suggestions = model.kneighbors(query, n_neighbors=n_neighbors)

    return suggestions[0]

# -----------------------------------
# Streamlit UI
# -----------------------------------
selected_book = st.selectbox("Select a Book", book_titles)

if st.button("Recommend"):
    suggestions = recommend_book(selected_book, model, book_sparse)

    st.subheader(f"Recommended Books for: **{selected_book}**")
    
    for idx in suggestions[1:]:  # skip the book itself
        st.write("📘", book_pivot.index[idx])