🚀 Flask User Management REST API

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?logo=flask)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A simple **REST API built using Flask** that performs CRUD operations on user data stored in an **in-memory database**.
This project is developed as part of **Python Developer Internship – Task 4**.

---

📌 Project Objective

✔ Build a REST API using Flask
✔ Perform **GET, POST, PUT, DELETE** operations
✔ Test API with Thunder Client / Postman
✔ Understand API fundamentals & JSON response handling

---

 📁 Project Structure

```
📦 Flask-User-API
 ┣ 📜 app.py        → Main Flask Application
 ┗ 📜 README.md     → Project Documentation
```

---

## ⚙️ Technologies Used

| Tool           | Purpose          |
| -------------- | ---------------- |
| Python         | Backend language |
| Flask          | Web framework    |
| Thunder Client | API testing      |
| JSON           | Data format      |

---

🚀 How to Run

🔹 1️⃣ Install Flask

```sh
pip install flask
```

🔹 2️⃣ Run the API

```sh
python app.py
```

You will see:

```
 * Running on http://127.0.0.1:5000
```

---

## 📡 API Endpoints

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/`           | API running status      |
| GET    | `/users`      | Get all users           |
| GET    | `/users/<id>` | Get user by ID          |
| POST   | `/users`      | Create a new user       |
| PUT    | `/users/<id>` | Update an existing user |
| DELETE | `/users/<id>` | Delete a user           |

---

🧪 Sample API Request

 ➤ Create User (POST)

🔹 URL: `http://127.0.0.1:5000/users`
🔹 JSON Body:

```json
{
  "name": "Anjelina",
  "email": "anjelina@gmail.com"
}
```

🔹 Response:

```json
{
  "id": 1,
  "name": "Anjelina",
  "email": "anjelina@gmail.com"
}
```

---

📷 Screenshots 
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4ad8b62a-19f7-411c-8944-c32382131eb4" />


 ✔ API Running Output

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c04a4ac5-11b5-43ac-ba28-18fbdc2cb0eb" />


 ✔ POST Request – User Created

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/8016c306-6bc6-4af0-b936-7f772cc12e12" />


 ✔ GET Request – Fetch all users

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7c9a04db-d054-4b29-8002-7639e7333d6e" />


---

🧠 What I Learned

✔ How REST APIs work
✔ Handling JSON in Flask
✔ Testing APIs with Thunder Client
✔ CRUD operations and route creation



 👩‍💻 Author

  Anjelina Princy A
💼 Python Developer Intern
📧 anjelinaprincyaruldass@gmail.com
⭐ GitHub: [https://github.com/Anjelina-princy14](https://github.com/Anjelina-princy14)

---

📢 Final Note

This project demonstrates API fundamentals clearly and can be extended to:

🔹 Use real database (MySQL, MongoDB)
🔹 Add Authentication
🔹 Deploy online

---

