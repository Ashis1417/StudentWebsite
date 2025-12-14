from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ashish@2007",
    database="student_db",
    auth_plugin="mysql_native_password"
)

cursor = conn.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        roll = request.form["roll"]
        name = request.form["name"]
        course = request.form["course"]
        marks = request.form["marks"]

        sql = "INSERT INTO students (roll, name, course, marks) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (roll, name, course, marks))
        conn.commit()

        return redirect("/view")

    return render_template("add.html")

@app.route("/view")
def view():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    return render_template("view.html", students=data)

if __name__ == "__main__":
    app.run(debug=True)
