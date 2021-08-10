from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Task
from flask.typing import ResponseReturnValue
from typing import Optional

main = Blueprint("main", __name__)


@main.route("/")
def index() -> ResponseReturnValue:
    tasks: list[Task] = Task.query.order_by(Task.position.asc().nullslast()).all()
    return render_template("index.html", tasks=tasks)


@main.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
    tasks = Task.query.all()
    return render_template("task_list.html", tasks=tasks)


@main.route("/complete/<int:task_id>")
def complete(task_id: int) -> ResponseReturnValue:
    task: Optional[Task] = Task.query.get(task_id)
    if task:
        task.done = True
        db.session.commit()
    return redirect(url_for("main.index"))


@main.route("/delete/<int:task_id>")
def delete(task_id: int) -> ResponseReturnValue:
    task: Optional[Task] = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for("main.index"))


@main.route("/reorder", methods=["POST"])
def reorder() -> tuple[str, int]:
    data: dict = request.get_json()
    new_order: list[int] = data.get("order", [])
    for index, task_id in enumerate(new_order):
        task: Optional[Task] = Task.query.get(task_id)
        if task:
            task.position = index
    db.session.commit()
    return "", 204
