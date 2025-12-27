from flask import Flask, render_template, request, redirect
from flask import jsonify
import random


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

@app.route("/ai")
def ai_page():
    return render_template("ai_chat.html")


# 🧠 AI ASSISTANT
@app.route("/ai-chat", methods=["POST"])
def ai_chat():
    user_msg = request.json.get("message","").lower()

    if "gpa" in user_msg:
        reply = "📊 Improve GPA by revising daily, solving past papers and managing your time using weekly planners."

    elif "fail" in user_msg or "low marks" in user_msg:
        reply = "😔 Failure is not the end. Identify weak subjects, meet your teachers and practice consistently."

    elif "skills" in user_msg:
        reply = "💡 Learn Python, SQL, GitHub, Data Analysis and AI tools to build a strong career profile."

    elif "internship" in user_msg:
        reply = "🧑‍💼 Start internships from 3rd semester, build projects and connect with seniors on LinkedIn."

    elif "courses" in user_msg or "subjects" in user_msg:
        reply = "📚 Recommended subjects: Data Structures, Database Systems and Intro to AI."

    elif "hello" in user_msg or "hi" in user_msg:
        reply = "Hello 👋 I am Uni Fellow AI. How can I help you today?"

    else:
        reply = random.choice([
            "That’s interesting, can you explain more?",
            "I am here to guide your academic journey.",
            "Please share more details so I can assist better."
        ])

    return jsonify({"reply": reply})


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


