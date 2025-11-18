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
Awesome! 🎉 Since you installed Postman, you're now ready to test your Flask REST API in a professional way. Here's a **simple guide** to help you test all routes of your API using Postman — step by step 👇

---

# 🧪 Testing Your Flask API with Postman

> **Make sure your Flask app is running!**
> Open your terminal and run:

```sh
python app.py
```

You should see:

```
Running on http://127.0.0.1:5000/
```

Now we're ready!

---

## 🔹 1. Test API Status (`GET /`)

**In Postman:**

1. Click **+ New** or `+` tab to open a new request.
2. Select **GET** as method.
3. Enter URL:

```
http://127.0.0.1:5000/
```

4. Click **Send**.

🟢 You should see:

```json
{
  "message": "User API is running"
}
```

---

## 🔹 2. Create a User (`POST /users`)

1. Click **+ New** tab again.
2. Set **Method:** `POST`
3. Enter URL:

```
http://127.0.0.1:5000/users
```

4. Go to **Body** > select **raw**, then choose `JSON` from dropdown.
5. Paste this JSON:

```json
{
  "name": "Anjelina Princy a",
  "email": "anjelinaprincyaldass@gmail.com"
}
``` 

6. Click **Send**.
   <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f65b1c11-cb18-4838-b3d6-b85ced7537a5" />




 🔹 3. Get All Users (`GET /users`)

1. Open a new tab → method `GET`
2. URL:

```
http://127.0.0.1:5000/users
```

3. Click Send

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f5c7c40b-d444-4f29-84db-e0ba5320b8a3" />


 🔹 4. Update a User (`PUT /users/1`)

1. New tab → Method `PUT`
2. URL:

```
http://127.0.0.1:5000/users/1
```

3. Go to **Body → raw → JSON**
4. Paste:

```json
{
  "name": "Angel",
  "email": "angel@gmail.com"
}
```

5. Click Send.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/4b62195d-8756-48ad-8886-a7ef5ab2b797" />


 🔹 5. Delete User (`DELETE /users/1`)

1. New tab → Method `DELETE`
2. URL:

```
http://127.0.0.1:5000/users/1
```

3. Click Send

🟢 You’ll see:

```json
{
  "message": "User deleted successfully"
}
```

---

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/36f54b56-4680-4065-b97d-6ed92b58c1ff" />



🧪 Sample API Request using Thunder Client 

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

