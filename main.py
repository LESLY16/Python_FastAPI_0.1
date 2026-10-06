# main.py
from fastapi import FastAPI  # type: ignore
from db import get_conn
from fetch import fetch_and_store

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/init")
def init():
    fetch_and_store()
    return {"message": "Data fetched & stored"}

@app.get("/posts")
def get_posts():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM posts")
    return cur.fetchall()
