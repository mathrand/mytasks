# 📝 My Tasks

**My Tasks** is a lightweight, Flask-based to-do list application powered by SQLite. It supports task creation, completion, deletion, and drag-and-drop reordering.

---

## 🚀 Features

- **Add New Tasks Instantly**
  Submit tasks via a form and see them appear immediately without refreshing the page.

- **Dynamic Task List Rendering**
  Uses AJAX to update the task list in real-time with smooth DOM replacement.

- **Drag-and-Drop Reordering**
  Tasks can be rearranged using SortableJS, with order saved to the backend.

- **Mark Tasks as Complete ✅**
  Toggle task status to visually strike through completed items.

- **Delete Tasks 🗑️**
  Remove tasks instantly with a single click.

- **Responsive UI**
  Built with Bootstrap for a clean, mobile-friendly layout.

- **Persistent Storage**
  Tasks are stored in a database and persist across sessions.

---

## ⚙️ Installation

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

---

## 🚀 Running the Application

### Development (Flask)

```bash
./venv/bin/python3 -m flask run
```

### Production

#### Linux / macOS (Gunicorn)

```bash
gunicorn app:app
```

#### Windows (Waitress)

```bash
waitress-serve --listen=0.0.0.0:8000 app:app
```

> ⚠️ Flask’s built-in server is for development only. Use Gunicorn or Waitress for production deployments.

---

## ✅ Running Tests

Use `pytest` to run the test suite:

```bash
./venv/bin/python3 -m pytest
```
