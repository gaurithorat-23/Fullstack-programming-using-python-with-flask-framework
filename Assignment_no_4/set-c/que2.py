
from flask import Flask

app = Flask(__name__)

@app.route('/employee/<name>')
def employee(name):
    return f"Hello {name}, welcome to the Employee Portal!"

if __name__ == '__main__':
    app.run(debug=True)