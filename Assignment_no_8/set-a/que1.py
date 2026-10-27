from flask import Flask
import psycopg2

app = Flask(__name__)

def database_connection():
    return psycopg2.connect(
        host="localhost",
        database="Hospital",
        user="postgres",
        password="root"
    )

@app.route('/')
def home():
   
    return "Your Database is Connected Successfully!"

if __name__ == '__main__':
    app.run(debug=True)