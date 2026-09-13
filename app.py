"""
CampusCompass

A web application that helps university students manage their academic life
by tracking tasks, assignments, subjects, and attendance.

"""


# Portions of this project were developed with the assistance of ChatGPT (OpenAI)
# for debugging, code explanations, and implementation guidance
# in accordance with CS50's final project policy.
# All final design decisions, testing, and integration were completed by the author.


# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


# Create Flask application
app = Flask(__name__)
app.secret_key = "campuscompass_secret_key"


# Home Page
@app.route("/")
def index():

    if "user_id" in session:
        return redirect(url_for("dashboard"))

    return render_template("index.html")


# User Registration
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        # Get data from the registration form
        full_name = request.form.get("full_name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirm_password")

        # Check if passwords match
        if password != confirmation:
            return "Passwords do not match"

        # Hash the password before storing
        password_hash = generate_password_hash(password)

        connection = sqlite3.connect("campuscompass.db")
        cursor = connection.cursor()

        # Insert the new user into the database
        cursor.execute(
            """INSERT INTO users (full_name, username, email, password_hash)
            VALUES (?, ?, ?, ?)
            """,
            (full_name, username, email, password_hash)
        )

        # Save the new user and close the connection
        connection.commit()
        connection.close()

        return redirect(url_for("login"))

    else:
        return render_template("register.html")


# User Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        # Get login credentials
        username = request.form.get("username")
        password = request.form.get("password")

        connection = sqlite3.connect("campuscompass.db")
        cursor = connection.cursor()

        # Retrieve user from the database
        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        # Fetch the matching user record
        user = cursor.fetchone()

        connection.close()

        if user is None:
            return "User does not exist"

        # Verify the password
        if not check_password_hash(user[4], password):
            return "Incorrect password"

        # Store the user's ID in the session
        session["user_id"] = user[0]

        return redirect(url_for("dashboard"))

    else:
        return render_template("login.html")


# Dashboard
@app.route("/dashboard")
def dashboard():

    # Redirect unauthenticated users
    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("campuscompass.db")
    cursor = connection.cursor()

    # Fetch the logged-in user's name
    cursor.execute(
        "SELECT full_name FROM users WHERE id = ?", (session["user_id"],)
    )

    user = cursor.fetchone()

    # Fetch all tasks belonging to the user
    cursor.execute("""
    SELECT id, title, description, due_date, status
    FROM tasks
    WHERE user_id = ?
    ORDER BY due_date
    """, (session["user_id"],))

    tasks = cursor.fetchall()

    connection.close()

    return render_template("dashboard.html", user=user, tasks=tasks)


# Logout
@app.route("/logout")
def logout():

    # Clear the current user's session
    session.clear()

    # Redirect to the home page
    return redirect(url_for("index"))


# Add Task
@app.route("/add_task", methods=["GET", "POST"])
def add_task():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        # Get task details from the form
        title = request.form.get("title")
        description = request.form.get("description")
        due_date = request.form.get("due_date")

        # Connect to the database
        connection = sqlite3.connect("campuscompass.db")
        cursor = connection.cursor()

        # Save the new task in the database
        cursor.execute("""
        INSERT INTO tasks (user_id, title, description, due_date)
        VALUES (?, ?, ?, ?)
        """, (
            session["user_id"],
            title,
            description,
            due_date
        ))

        # Save changes and close the connection
        connection.commit()
        connection.close()

        return redirect(url_for("dashboard"))

    return render_template("add_task.html")


# Mark Task as Completed
@app.route("/complete_task/<int:task_id>")
def complete_task(task_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("campuscompass.db")
    cursor = connection.cursor()

    # Update the task status to Completed
    cursor.execute("""
    UPDATE tasks
    SET status = 'Completed'
    WHERE id = ? AND user_id = ?
    """, (task_id, session["user_id"]))

    connection.commit()
    connection.close()

    return redirect(url_for("dashboard"))


# Delete Task
@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("campuscompass.db")
    cursor = connection.cursor()

    # Delete the selected task from the database
    cursor.execute("""
    DELETE FROM tasks
    WHERE id = ? AND user_id = ?
    """, (task_id, session["user_id"]))

    connection.commit()
    connection.close()

    return redirect(url_for("dashboard"))


# Add Subject
@app.route("/add_subject", methods=["GET", "POST"])
def add_subject():

    # Redirect unauthenticated users
    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        # Get subject name from the form
        subject_name = request.form.get("subject_name")

        connection = sqlite3.connect("campuscompass.db")
        cursor = connection.cursor()

        # Save the subject to the attendance table
        cursor.execute("""
        INSERT INTO attendance (user_id, subject_name)
        VALUES (?, ?)
        """, (
            session["user_id"],
            subject_name
        ))

        connection.commit()
        connection.close()

        return redirect(url_for("attendance"))

    return render_template("add_subject.html")


# Attendance Dashboard
@app.route("/attendance")
def attendance():

    # Redirect unauthenticated users
    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("campuscompass.db")
    cursor = connection.cursor()

    # Retrieve all subjects for the logged-in user
    cursor.execute("""
    SELECT id, subject_name, classes_attended, total_classes
    FROM attendance
    WHERE user_id = ?
    ORDER BY subject_name
    """, (session["user_id"],))

    subjects = cursor.fetchall()

    connection.close()

    return render_template("attendance.html", subjects=subjects)


# Mark Class as Attended
@app.route("/attended/<int:subject_id>")
def attended(subject_id):

    # Redirect unauthenticated users
    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("campuscompass.db")
    cursor = connection.cursor()

    # Increase both attended and total classes
    cursor.execute("""
    UPDATE attendance
    SET
    classes_attended = classes_attended + 1,
    total_classes = total_classes + 1
    WHERE id = ? AND user_id = ?
    """, (subject_id, session["user_id"]))

    connection.commit()
    connection.close()

    return redirect(url_for("attendance"))


# Mark Class as Missed
@app.route("/missed/<int:subject_id>")
def missed(subject_id):

    # Redirect unauthenticated users
    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("campuscompass.db")
    cursor = connection.cursor()

    # Increase only the total number of classes
    cursor.execute("""
    UPDATE attendance
    SET
    total_classes = total_classes + 1
    WHERE id = ? AND user_id = ?
    """, (subject_id, session["user_id"]))

    connection.commit()
    connection.close()

    return redirect(url_for("attendance"))


# Delete Subject
@app.route("/delete_subject/<int:subject_id>")
def delete_subject(subject_id):

    # Redirect unauthenticated users
    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("campuscompass.db")
    cursor = connection.cursor()

    # Remove the selected subject from the database
    cursor.execute("""
    DELETE FROM attendance
    WHERE id = ? AND user_id = ?
    """, (subject_id, session["user_id"]))

    connection.commit()
    connection.close()

    return redirect(url_for("attendance"))



# Add Class
@app.route("/add_class", methods=["GET", "POST"])
def add_class():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        subject_name = request.form.get("subject_name")

        day = request.form.get("day")

        start_time = request.form.get("start_time")

        end_time = request.form.get("end_time")

        repeat = request.form.get("repeat")

        connection = sqlite3.connect("campuscompass.db")

        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO timetable
        (user_id, subject_name, day, start_time, end_time, repeat)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            session["user_id"],
            subject_name,
            day,
            start_time,
            end_time,
            repeat
        ))

        connection.commit()

        connection.close()

        return redirect(url_for("timetable"))

    return render_template("add_class.html")


# Timetable
@app.route("/timetable")
def timetable():

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = sqlite3.connect("campuscompass.db")

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM timetable
    WHERE user_id = ?
    ORDER BY day, start_time
    """, (session["user_id"],))

    classes = cursor.fetchall()

    connection.close()

    return render_template(
        "timetable.html",
        classes=classes
    )



# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)
