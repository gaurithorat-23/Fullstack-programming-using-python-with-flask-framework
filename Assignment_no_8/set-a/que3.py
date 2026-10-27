from flask import Flask
import psycopg2

app =Flask(__name__)

@app.route('/insert')
def insert_students():
    try:
        conn = psycopg2.connect(
            dbname="student",
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
        cur.executemany("INSERT INTO Students (name, age, course) VALUES (%s, %s, %s);", students)
        conn.commit()
        cur.close()
        conn.close()
        return "5 Student Records Inserted Successfully"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)