# fetch.py
import json
from urllib.request import urlopen
from db import get_conn

def fetch_and_store():
    url = "https://jsonplaceholder.typicode.com/posts"
    with urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))

    conn = get_conn()
    cur = conn.cursor()

    for item in data:
        cur.execute("INSERT INTO posts VALUES (?, ?, ?)",
                    (item["id"], item["title"], item["body"]))

    conn.commit()
    conn.close()
