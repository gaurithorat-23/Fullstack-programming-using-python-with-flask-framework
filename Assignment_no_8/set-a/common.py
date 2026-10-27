from flask import Flask
import psycopg2
app = Flask(__name__)
def db_connect():
    return psycopg2.connect(
        dbname="samarth",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

@app.route('/')
def home():
    return "Your Database is Connected Successfully!"
@app.route('/student_table')
def create_table():
    conn = None
    try:
        conn = db_connect()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student(
                stu_id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                class VARCHAR(100)
            );
        """)
        conn.commit()
        cur.close()
        return "student table is created successfully!"
    except psycopg2.Error as e:
        if conn:
            conn.rollback()
        return f"Database error: {e}", 500

    finally:
        if conn:
            conn.close()

@app.route('/insert')
def insert_student():
    try:
        conn = psycopg2.connect(
            dbname="samarth",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()
        students = [
            ('Mahir', 24, 'Computer Science'),
            ('Gauravi', 22, 'Technology'),
            ('Samaya', 20, 'Data Analyst'),
            ('Riyansh', 23, 'Cyber Security'),
            ('Daya', 21, 'AI')
        ]
        cur.executemany("INSERT INTO Student (name, age, class) VALUES (%s, %s, %s);", students)
        conn.commit()
        cur.close()
        conn.close()
        return "5 Student Records Inserted Successfully"
    except Exception as e:
        return f"Error: {e}"            


if __name__ == "__main__":
    app.run(debug=True)
