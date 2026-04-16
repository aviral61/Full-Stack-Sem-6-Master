from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
students = [
    {"id": 1, "name": "Aviral", "age": 21, "course": "CSE"},
    {"id": 2, "name": "Rahul", "age": 22, "course": "IT"}
]

# Home Route
@app.route('/')
def home():
    return jsonify({"message": "Student API is running successfully!"})


# GET All Students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)


# GET Student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student["id"] == id:
            return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


# CREATE Student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    new_student = {
        "id": students[-1]["id"] + 1 if students else 1,
        "name": data.get("name"),
        "age": data.get("age", None),       # ✅ FIX
        "course": data.get("course", None)  # ✅ FIX
    }

    students.append(new_student)
    return jsonify(new_student), 201


# UPDATE Student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    for s in students:
        if s["id"] == id:
            s["name"] = data.get("name", s["name"])
            s["age"] = data.get("age", s.get("age"))
            s["course"] = data.get("course", s.get("course"))
            return jsonify(s)

    return {"error": "Not found"}, 404

# DELETE Student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    for student in students:
        if student["id"] == id:
            students.remove(student)
            return jsonify({"message": "Student deleted successfully"})
    return jsonify({"error": "Student not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)