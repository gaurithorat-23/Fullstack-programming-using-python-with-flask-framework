from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

# Connect to database
def db_connect():
    return psycopg2.connect(
        dbname="mandir",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )


# Create Donation table
def create_table():
    con = db_connect()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Donation1 (
            Donation_ID SERIAL PRIMARY KEY,
            Donor_Name VARCHAR(100),
            Amount FLOAT,
            Purpose VARCHAR(100)
        )
    """)

    con.commit()
    cur.close()
    con.close()


# Insert donation
@app.route("/", methods=["GET", "POST"])
def add_donation():
    if request.method == "POST":
        donor_name = request.form["Donor_Name"]
        amount = request.form["Amount"]
        purpose = request.form["Purpose"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "INSERT INTO Donation1 (Donor_Name, Amount, Purpose) VALUES (%s, %s, %s)",
            (donor_name, amount, purpose)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/donation")

    return render_template("add.html")


# Display donations
@app.route("/donation")
def display_donations():
    con = db_connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM Donation1 ORDER BY Donation_ID")
    donations = cur.fetchall()

    cur.execute("SELECT COALESCE(SUM(Amount), 0) FROM Donation1")
    total = cur.fetchone()[0]

    cur.close()
    con.close()

    return render_template("donation.html", donations=donations, total=total)


# Update donation amount
@app.route("/update", methods=["GET", "POST"])
def update_donation():
    if request.method == "POST":
        donation_id = request.form["Donation_ID"]
        amount = request.form["Amount"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "UPDATE Donation1 SET Amount = %s WHERE Donation_ID = %s",
            (amount, donation_id)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/donation")

    return render_template("update.html")


# Delete donation
@app.route("/delete", methods=["GET", "POST"])
def delete_donation():
    if request.method == "POST":
        donation_id = request.form["Donation_ID"]

        con = db_connect()
        cur = con.cursor()

        cur.execute(
            "DELETE FROM Donation1 WHERE Donation_ID = %s",
            (donation_id,)
        )

        con.commit()
        cur.close()
        con.close()

        return redirect("/donation")

    return render_template("delete.html")


if __name__ == "__main__":
    create_table()
    app.run(debug=True)
