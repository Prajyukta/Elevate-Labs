import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:8000"  # Your FastAPI URL

st.title("📚 Bookstore Dashboard")

# Sidebar menu
menu = ["View Books", "Add Book", "Update Book", "Delete Book", "Analytics"]
choice = st.sidebar.selectbox("Menu", menu)

# ----------------- VIEW BOOKS -----------------
if choice == "View Books":
    st.subheader("All Books")
    response = requests.get(f"{API_URL}/books")
    books = response.json()
    df = pd.DataFrame(books)
    st.dataframe(df)

# ----------------- ADD BOOK -----------------
elif choice == "Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    price = st.number_input("Price", min_value=0.0)
    if st.button("Add Book"):
        payload = {"title": title, "author": author, "price": price}
        res = requests.post(f"{API_URL}/books", json=payload)
        st.success(f"Added: {res.json()}")

# ----------------- UPDATE BOOK -----------------
elif choice == "Update Book":
    st.subheader("Update Book")
    book_id = st.number_input("Book ID", min_value=1)
    title = st.text_input("New Title")
    author = st.text_input("New Author")
    price = st.number_input("New Price", min_value=0.0)
    if st.button("Update Book"):
        payload = {"title": title, "author": author, "price": price}
        res = requests.put(f"{API_URL}/books/{book_id}", json=payload)
        st.success(f"Updated: {res.json()}")

# ----------------- DELETE BOOK -----------------
elif choice == "Delete Book":
    st.subheader("Delete Book")
    book_id = st.number_input("Book ID to Delete", min_value=1)
    if st.button("Delete Book"):
        res = requests.delete(f"{API_URL}/books/{book_id}")
        st.success(f"Deleted: {res.json()}")

# ----------------- ANALYTICS -----------------
elif choice == "Analytics":
    st.subheader("Books Analytics")
    response = requests.get(f"{API_URL}/books")
    books = response.json()
    df = pd.DataFrame(books)
    if not df.empty:
        # Books per Author
        author_count = df['author'].value_counts().reset_index()
        author_count.columns = ['Author', 'Books Count']
        fig = px.bar(author_count, x='Author', y='Books Count', title="Books per Author")
        st.plotly_chart(fig)
        
        # Total value of books per author
        author_price = df.groupby('author')['price'].sum().reset_index()
        fig2 = px.pie(author_price, names='author', values='price', title="Total Price per Author")
        st.plotly_chart(fig2)
