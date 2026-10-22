from flask import Flask, request, redirect

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Complete assignment", "done": False},
    {"id": 2, "title": "Learn Docker and Kubernetes", "done": False}
]

@app.route("/")
def home():
    html = """
    <html>
    <head>
        <title>Student Task Manager</title>
        <style>
            body { font-family: Arial; max-width: 700px; margin: 40px auto; }
            h1 { color: #2457a7; }
            li { margin: 12px 0; }
            input, button { padding: 10px; }
        </style>
    </head>
    <body>
        <h1>Student Task Manager</h1>
        <p>Manage your academic tasks in one place.</p>
        <form action="/add" method="post">
            <input name="title" placeholder="Enter a new task" required>
            <button type="submit">Add Task</button>
        </form>
        <h2>My Tasks</h2>
        <ul>
    """
    for task in tasks:
        status = "Completed" if task["done"] else "Pending"
        html += f"<li>{task['title']} — {status} "
        html += f"<a href='/complete/{task['id']}'>Complete</a></li>"
    html += "</ul></body></html>"
    return html

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    if title:
        tasks.append({
            "id": max([t["id"] for t in tasks], default=0) + 1,
            "title": title,
            "done": False
        })
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
    return redirect("/")

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
