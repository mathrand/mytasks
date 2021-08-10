import pytest
from app import app
from models import db, Task


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_add_task(client):
    response = client.post("/add", data={"title": "Buy milk"}, follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        task = Task.query.filter_by(title="Buy milk").first()
        assert task is not None
        assert not task.done


def test_complete_task(client):
    with app.app_context():
        task = Task(title="Walk dog")
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    response = client.get(f"/complete/{task_id}", follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        task = Task.query.get(task_id)
        assert task.done


def test_delete_task(client):
    with app.app_context():
        task = Task(title="Delete me")
        db.session.add(task)
        db.session.commit()
        task_id = task.id

    response = client.get(f"/delete/{task_id}", follow_redirects=True)
    assert response.status_code == 200
    with app.app_context():
        task = Task.query.get(task_id)
        assert task is None


def test_reorder_tasks(client):
    with app.app_context():
        t1 = Task(title="Task 1", position=0)
        t2 = Task(title="Task 2", position=1)
        t3 = Task(title="Task 3", position=2)
        db.session.add_all([t1, t2, t3])
        db.session.commit()

        # Reorder: Task 3, Task 1, Task 2
        new_order = [t3.id, t1.id, t2.id]
        response = client.post("/reorder", json={"order": new_order})
        assert response.status_code == 204

        # Verify new positions
        reordered = Task.query.order_by(Task.position).all()
        assert [task.id for task in reordered] == new_order
