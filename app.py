from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database"
users = {}
next_id = 1


@app.route("/")
def home():
    # For: http://127.0.0.1:5000/
    return jsonify({"message": "User API is running"})


# GET all users: http://127.0.0.1:5000/users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values())), 200


# GET one user: http://127.0.0.1:5000/users/1
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200


# CREATE user (POST): http://127.0.0.1:5000/users
# JSON body: {"name": "...", "email": "..."}
@app.route("/users", methods=["POST"])
def create_user():
    global next_id

    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Both 'name' and 'email' are required"}), 400

    user = {
        "id": next_id,
        "name": name,
        "email": email
    }
    users[next_id] = user
    next_id += 1

    # Example expected: {"id": 1, "name": "...", "email": "..."}
    return jsonify(user), 201


# UPDATE user (PUT): http://127.0.0.1:5000/users/1
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Only update what is provided
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])

    # Example expected after update:
    # {"id": 1, "name": "New Name", "email": "same@email.com"}
    return jsonify(user), 200


# DELETE user: http://127.0.0.1:5000/users/1
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Expected: {"message": "User deleted successfully"}
    return jsonify({"message": "User deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
