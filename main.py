from flask import Flask, render_template, request, redirect, url_for, flash, session
from student import Student

app = Flask(__name__)
app.secret_key = "message"
query = Student()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        if query.check_login(email, password):
            return redirect(url_for('home'))  # Redirect to the home page/dashboard
        else:
            flash("Invalid email/password.Try again.", "danger")

    return render_template("login.html")


@app.route("/create-account", methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        if query.create_account(email, password):
            return redirect(url_for('login'))  # Redirect to login page after creating account
        else:
            flash("Email already in use. Try a different email.", "danger")

    return render_template("create-account.html")

@app.route("/home")
def home():
    data = query.fetch_all()
    if data is None:
        data = []
    return render_template("index.html", students=data)

@app.route("/post", methods=["POST"])
def post():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form["name"]
        student_id = request.form["student_id"]
        email = request.form["email"]
        phone = request.form["phone"]
        gender = request.form["gender"]

        query.post(name, student_id, email, phone, gender)
        return redirect(url_for("home"))

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    updates = {}
    if request.form.get("_method") == "PUT":
        flash("Data Updated Successfully")
        if request.form["name"]: updates["name"] = request.form["name"]
        if request.form["student_id"]: updates["student_id"] = request.form["student_id"]
        if request.form["email"]: updates["email"] = request.form["email"]
        if request.form["phone"]: updates["phone"] = request.form["phone"]
        if request.form["gender"]: updates["gender"] = request.form["gender"]

        query.update(id,**updates)
        return redirect(url_for("home"))

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    if request.method in ["POST", "DELETE"]:  # Ensure both methods are accepted
        query.delete(id)
        flash("Data Deleted Successfully")
        return redirect(url_for("home"))
    return "Method Not Allowed", 405

@app.route("/logout")
def logout():
    session.clear()  # Clears all session data
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)