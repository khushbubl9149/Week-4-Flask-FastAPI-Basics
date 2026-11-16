
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Student Management API",
    description="A simple REST API built with FastAPI",
    version="1.0.0"
)

# Temporary storage
students = {
    1: {"name": "Rahul", "age": 22, "course": "Python"},
    2: {"name": "Priya", "age": 23, "course": "Data Science"}
}

# Data validation model
class Student(BaseModel):
    name: str
    age: int
    course: str


# 1. GET - Get all students
@app.get("/students")
def get_students():
    return students


# 2. GET - Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    return students[student_id]


# 3. POST - Add a new student
@app.post("/students")
def add_student(student: Student):
    student_id = max(students.keys(), default=0) + 1

    students[student_id] = student.model_dump()

    return {
        "message": "Student added successfully",
        "student_id": student_id,
        "student": students[student_id]
    }


# 4. PUT - Update student details
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    students[student_id] = student.model_dump()

    return {
        "message": "Student updated successfully",
        "student": students[student_id]
    }


# 5. DELETE - Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }
