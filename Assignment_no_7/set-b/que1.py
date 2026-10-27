from flask import Flask ,request, jsonify
app = Flask(__name__)
products = [
    {"name":"Laptop",
      "Price": 50000,
        "Category":"Electronic"}
]
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route("/addproducts", methods = ["POST"])
def add_product():
    data = request.get_json()

    name = data.get("name")
    price = data.get("price")
    category = data.get("category")

    product = {
        "name":name,
        "price":price,
        "category":category
    }
    products.append(product)
    return jsonify(
        {       "msg":"Product added sucessfully"}
    )

if __name__ == '__main__':
    app.run(debug = True)