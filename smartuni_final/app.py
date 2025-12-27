from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory storage
chat_messages = []
announcements = []
registered_societies = []

# LOGIN
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form["role"]
        return redirect("/faculty" if role == "Faculty" else "/student")
    return render_template("login.html")

# DASHBOARDS
@app.route("/student")
def student_dashboard():
    return render_template("student_dashboard.html")

@app.route("/faculty")
def faculty_dashboard():
    return render_template("faculty_dashboard.html")

# CHAT
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        chat_messages.append(request.form["message"])
    return render_template("chat.html", messages=chat_messages)

# 🧠 AI ASSISTANT
@app.route("/ai", methods=["GET", "POST"])
def ai():
    advice = skills = future = ""
    if request.method == "POST":
        gpa = float(request.form["gpa"])
        course = request.form["course"].lower()

        if gpa < 2.5:
            future = "Improve academic foundation."
            skills = "Time management, study skills"
        elif gpa < 3.5:
            future = "Strengthen technical profile."
            skills = "Python, Git, Data Structures"
        else:
            future = "Internships & research recommended."
            skills = "AI/ML, leadership"

        advice = "Choose career path aligned with your courses."

    return render_template("ai.html", advice=advice, skills=skills, future=future)

# 📢 FACULTY ANNOUNCEMENTS (POST + VIEW)
@app.route("/faculty/announcements", methods=["GET", "POST"])
def faculty_announcements():
    if request.method == "POST":
        announcements.append(request.form["announcement"])
    return render_template("announcements_faculty.html", announcements=announcements)

# 📢 STUDENT ANNOUNCEMENTS (VIEW ONLY)
@app.route("/student/announcements")
def student_announcements():
    return render_template("announcements_student.html", announcements=announcements)

# SOCIETIES
@app.route("/societies", methods=["GET", "POST"])
def societies():
    message = ""
    if request.method == "POST":
        registered_societies.append(request.form["society"])
        message = "Registration successful!"
    return render_template("societies.html", registered=registered_societies, message=message)

if __name__ == "__main__":
    app.run(debug=True)



