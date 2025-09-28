from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (dictionary for simplicity)
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# ---------------- Routes ---------------- #

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# GET a single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404


# POST - Add new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"id": new_id, "message": "User added successfully"}), 201


# PUT - Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json
    users[user_id].update(data)  # Update existing fields
    return jsonify({"message": "User updated successfully", "user": users[user_id]}), 200


# DELETE - Remove user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    del users[user_id]
    return jsonify({"message": "User deleted successfully"}), 200


# ---------------- Run App ---------------- #
if __name__ == "__main__":
    app.run(debug=True)
