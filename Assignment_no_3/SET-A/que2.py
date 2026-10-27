
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Name: Gauravi Thorat, Roll Number: 70"

if __name__ == '__main__':
    app.run(debug=True)