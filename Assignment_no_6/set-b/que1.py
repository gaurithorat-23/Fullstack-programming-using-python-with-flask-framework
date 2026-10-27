
from flask import Flask

app = Flask(__name__)

@app.route("/")
def student_info():
    student = {
        "name": "Gauravi Thorat",
        "rollno": "101",
        "age" : 21,
        "class" : "T.Y.BSc.(IT)"
    }

    return f"""
    <h2>Student Information</h2>
    Name: {student['name']}<br>
    Roll Number: {student['rollno']}<br>
    Age: {student['age']}<br>
    Class: {student['class']}<br>
   
    """

if __name__ == "__main__":
    app.run(debug=True)