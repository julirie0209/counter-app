# Counter App (Fullstack)

A simple fullstack counter application built with a React frontend and Flask backend.
The app allows users to increment, decrement, and reset a counter, with the value persisted using SQLite.

---

## 🛠 Tech Stack

* **Frontend:** React (Vite)
* **Backend:** Flask (Python)
* **Database:** SQLite
* **Communication:** REST API (fetch)

---

## 📁 Project Structure

```
counter-app/
  backend/
    server.py
    requirements.txt
    counter.db
  frontend/
    src/
    public/
    package.json
```

---

## 🚀 Getting Started

### 1. Clone the repository

```
git clone <your-repo-url>
cd counter-app
```

---

## 🔧 Backend Setup (Flask)

Navigate to the backend:

```
cd backend
```

Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
python server.py
```

Backend will run on:

```
http://127.0.0.1:5000
```

---

## 💻 Frontend Setup (React)

Open a new terminal and navigate to the frontend:

```
cd frontend
```

Install dependencies:

```
npm install
```

Start the development server:

```
npm run dev
```

Frontend will run on something like:

```
http://localhost:5173
```

---

## 🔗 API Endpoints

| Method | Endpoint                 | Description       |
| ------ | ------------------------ | ----------------- |
| GET    | `/api/counter`           | Get current count |
| POST   | `/api/counter/increment` | Increment counter |
| POST   | `/api/counter/decrement` | Decrement counter |
| POST   | `/api/counter/reset`     | Reset counter     |

---

## 💾 Persistence

The counter value is stored in a local SQLite database:

```
backend/counter.db
```

* Survives page refreshes
* Persists across backend restarts
* Resets only if the database file is deleted

---

## ⚠️ Notes

* Make sure the Flask backend is running before using the frontend
* CORS is enabled to allow communication between ports
* `.venv` and `node_modules` are excluded via `.gitignore`

---

## 🚀 Future Improvements

* Add Docker support
* Deploy frontend and backend
* Add authentication
* Replace SQLite with a cloud database
* Add tests

---

## 📌 Author

Built as a learning project to understand fullstack development with React and Flask.
