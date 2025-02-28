# FastAPI-SQLModel-PostgreSQL Game API

A simple REST API to manage games using **FastAPI**, **SQLModel**, and **PostgreSQL** (hosted on Azure).

## Features

- **CRUD Operations**: Create, Read, Update, and Delete games.
- **SQLModel** for database interactions.
- **FastAPI** for building RESTful APIs.
- **PostgreSQL** hosted on **Azure**.

## Requirements

- Python 3.8+
- PostgreSQL (Azure or Local)
- FastAPI & SQLModel

## Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/RahulMule/fastapi-sqlmodel-demo
cd fastapi-sqlmodel-demo
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

Update the `database/db.py` file with your **PostgreSQL connection string**:

```python
DATABASE_URL = "postgresql://username:password@hostname:port/database_name"
```

### 5️⃣ Run the Application

```bash
uvicorn app.main:app --reload
```

### 6️⃣ Access the API Docs

Once running, you can explore the API with **Swagger UI**:

- 🚀 Open: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## API Endpoints

### 📌 Create a Game

```http
POST /games/
```

**Request Body:**

```json
{
  "title": "Elden Ring",
  "genre": "RPG",
  "platform": "PC",
  "release_year": 2022
}
```

### 📌 Get All Games

```http
GET /games/
```

### 📌 Get a Single Game

```http
GET /games/{game_id}
```

### 📌 Update a Game

```http
PUT /games/{game_id}
```

**Request Body:**

```json
{
  "title": "Elden Ring: Shadow Edition",
  "genre": "RPG",
  "platform": "PC",
  "release_year": 2023
}
```

### 📌 Delete a Game

```http
DELETE /games/{game_id}
```

---

## 🔥 Technologies Used

- **FastAPI** - High-performance web framework
- **SQLModel** - ORM for structured data
- **PostgreSQL** - Database hosted on Azure
- **Uvicorn** - ASGI server

## 👨‍💻 Contributing

1. Fork the repo & create a new branch.
2. Make changes and commit them.
3. Open a Pull Request.

## 📜 License

This project is licensed under the **MIT License**.

---

🚀 Happy Coding! 🎮
