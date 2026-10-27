#dynamic course infooo



from flask import Flask

app=Flask(__name__)

app.route('/course/<course_name>')
def course(course_name):
    return f"Course Name:{course_name}<br>course Information:provides skills and knowldge."

if __name__=='__main__':
    app.run(debug=True)


