from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"name":"Watch", "Price": 5000, "Category":"Electronic"},
    {"name":"Ac", "Price": 40000, "Category":"Electronic"},
    {"name":"Mackbook", "Price": 100000, "Category":"Electronic"},

]
@app.route('/product', methods = ['GET'])
def product_details():

    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)