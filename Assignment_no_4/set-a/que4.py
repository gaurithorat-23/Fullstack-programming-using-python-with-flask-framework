#Create Flask routes for /home, /student, and /faculty displaying suitable messages. 

from flask import Flask

app=Flask(__name__)

@app.route('/home')
def home():
    return"Welcome to the home page"

@app.route('/student')
def student():
    return"This is about student details"

@app.route('/faculty')
def faculty():
    return"This is about faculty details"

if __name__=="__main__":
 app.run(debug=True)