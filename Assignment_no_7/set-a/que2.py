    
from flask import Flask, request, jsonify

app = Flask(__name__)

employee = [{"Department":"Mechanical",
            "Name":"Rahul"},
            {"Department":"Electronic",
             "name":"manoj"}]


@app.route('/employee', methods=['GET'])
def get_employee():
    return jsonify(employee)

@app.route('/addemployee', methods=['POST'])
def add_employee():
    data = request.get_json()

    employee.append(data)

    return jsonify({
        "msg": "Employee added successfully",
        "employee": data
    }), 201

if __name__ == '__main__':
    app.run(debug=True)



    
