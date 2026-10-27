
from flask import Flask
import psycopg2
app = Flask(__name__)
def db_connect():
    return psycopg2.connect(
        dbname="hospital",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
@app.route('/create_table')
def create_table():
    conn = None
    try:
        conn = db_connect()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS patient (
                patient_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                disease VARCHAR(100)
            );
        """)
        conn.commit()
        cur.close()
        return "Patient table is created successfully!"
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        return f"Database error: {e}", 500

    finally:
        if conn:
            conn.close()

@app.route('/insert_records')
def insert_patients():
    try:
        conn = db_connect()
        cur = conn.cursor()
        patients = [
            ("Mehul", 24, "Fever"),
            ("siya", 31, "Diabetes"),
            ("sumit", 45, "Hypertension"),
            ("Sneha", 28, "Asthma"),
            ("Vikrama", 52, "Arthritis")
        ]

        cur.executemany("INSERT INTO Patient(name,age,disease) VALUES(%s,%s,%s)",patients)
        conn.commit()
        cur.close()
        conn.close()

        return "5 record inserted sucessfully!"

    except Exception as e:
        return f"Error: {e}"

@app.route('/search_patient/<int:pid>')
def search_patient(pid):
    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Patient WHERE patient_id = %s;",(pid,))
        patient = cur.fetchone()

        cur.close()
        conn.close()

        if patient:
            return f"Patient Details : ID={patient[0]}, Name={patient[1]}, Age={patient[2]}, Disease={patient[3]}"
        else:
            return "No patient associated with that ID"

    except Exception as e:
        return f"Error : {e}"            


if __name__ == "__main__":
    app.run(debug=True)
