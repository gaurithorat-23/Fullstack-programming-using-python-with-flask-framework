
from flask import Flask
import psycopg2

app=Flask(__name__)

def db_connect():
    return psycopg2.connect(
        dbname='student',
        user='postgres',
        password='root',
        host='localhost',
        port='5432'
    )

@app.route("/student_table")
def student_table():
    
    try:
        conn=db_connect()
        cur=conn.cursor()
        cur.execute("""
CREATE TABLE IF NOT EXISTS student_table(
student_id SERIAL PRIMARY KEY,
name VARCHAR(100),
age INT,
class VARCHAR(100)
);
""")

        conn.commit()
        cur.close()
        conn.close()

        return"student table is created succesfully!"

    except Exception as e:
        return f"Error:{e}"


if __name__ == "__main__":
    app.run(debug=True)