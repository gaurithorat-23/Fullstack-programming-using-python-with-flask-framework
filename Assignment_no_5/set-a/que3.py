
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def rectangle():
    result = ""

    if request.method == 'POST':
        length = float(request.form['length'])
        breadth = float(request.form['breadth'])
        area = length * breadth
        result = str(area)

    return '''
        <form method="POST">
            Enter Length:
            <input type="number" step="any" name="length" required><br><br>
            Enter Breadth:
            <input type="number" step="any" name="breadth" required><br><br>
            <input type="submit" value="Calculate Area">
        </form>
    
    '''

if __name__ == '__main__':
    app.run(debug=True)