A minimal FastAPI application with SQLite database, built for learning, local development, and deployment on Render.

📁 Project Structure
Code
Small-Project-Python/
│
├── main.py
├── db.py
├── fetch.py
├── data.db
├── requirements.txt
├── README.md
│
├── venv/          # Local virtual environment (ignored in Git)
├── .venv/         # Alternative virtual environment (ignored)
└── __pycache__/   # Python cache (ignored)
🚀 Features
FastAPI backend

SQLite database (data.db)

Simple API routes

Ready for deployment on Render

Auto-generated API docs at /docs and /redoc

🔧 Installation (Local Development)
1. Clone the repository
Code
git clone <your-repo-url>
cd Small-Project-Python
2. Create and activate a virtual environment
Code
python -m venv venv
venv\Scripts\activate
3. Install dependencies
Code
pip install -r requirements.txt
4. Run the FastAPI server
Code
uvicorn main:app --host 0.0.0.0 --port 8000
5. Open API documentation
Swagger UI → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

🗄️ Database
This project uses SQLite (data.db) for simplicity.

If you delete data.db, the app will recreate it (if your code handles that).

🌐 Deploying to Render
1. Push your project to GitHub
Make sure .gitignore excludes:

Code
venv/
.venv/
__pycache__/
data.db
2. Create a new Web Service on Render
Runtime: Python

Build Command:

Code
pip install -r requirements.txt
Start Command:

Code
uvicorn main:app --host 0.0.0.0 --port ${PORT}
3. Deploy
Render will build your app and give you a public URL.

📦 requirements.txt Example
Your file should include at least:

Code
fastapi
uvicorn
Add any other libraries your project uses.

🧪 Testing the API
Use browser or tools like:

Code
curl http://localhost:8000/
or Postman / Thunder Client.

📜 License
This project is for learning and personal development.