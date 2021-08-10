#!/usr/bin/env python3

import os
from flask import Flask
from models import db
from routes import main

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Task

db_path = os.getenv("TASKS_DB_PATH", "tasks.db")
db_uri = f"sqlite:///{db_path}"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(main)

if __name__ == "__main__":
    print(f"Using database at: {db_path}")

    with app.app_context():
        db.create_all()

    app.run(debug=True)
