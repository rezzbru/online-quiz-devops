from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": "New Delhi"
    },
    {
        "question": "Which language is used for web page structure?",
        "options": ["Python", "HTML", "Java", "C++"],
        "answer": "HTML"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Computer Processing User"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which technology is used for containerization?",
        "options": ["Docker", "Excel", "Photoshop", "PowerPoint"],
        "answer": "Docker"
    },
    {
        "question": "Which tool is commonly used for version control?",
        "options": ["Git", "Excel", "Chrome", "Word"],
        "answer": "Git"
    },
    {
        "question": "What does CI stand for?",
        "options": [
            "Continuous Integration",
            "Computer Installation",
            "Code Inspection",
            "Continuous Internet"
        ],
        "answer": "Continuous Integration"
    },
    {
        "question": "Which company developed Python?",
        "options": ["Microsoft", "Guido van Rossum", "Google", "Apple"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Which protocol is commonly used for secure websites?",
        "options": ["HTTP", "FTP", "HTTPS", "SMTP"],
        "answer": "HTTPS"
    },
    {
        "question": "What does API stand for?",
        "options": [
            "Application Programming Interface",
            "Application Program Internet",
            "Advanced Programming Input",
            "Applied Program Interface"
        ],
        "answer": "Application Programming Interface"
    },
    {
        "question": "Which platform is used to host Git repositories?",
        "options": ["GitHub", "YouTube", "Canva", "Google Maps"],
        "answer": "GitHub"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


@app.route("/submit", methods=["POST"])
def submit():
    score = 0

    for i, question in enumerate(questions):
        selected_answer = request.form.get(f"question_{i}")

        if selected_answer == question["answer"]:
            score += 1

    percentage = (score / len(questions)) * 100

    return render_template(
        "result.html",
        score=score,
        total=len(questions),
        percentage=percentage
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)