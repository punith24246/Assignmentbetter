import pytest
from app import create_app, db
from app.models import Comment

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client


def test_add_comment(client):
    response = client.post('/api/comments', json={'task_id': 1, 'content': 'Test comment'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['content'] == 'Test comment'


def test_edit_comment(client):
    client.post('/api/comments', json={'task_id': 1, 'content': 'Old content'})
    response = client.put('/api/comments/1', json={'content': 'Updated content'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['content'] == 'Updated content'


def test_delete_comment(client):
    client.post('/api/comments', json={'task_id': 1, 'content': 'To be deleted'})
    response = client.delete('/api/comments/1')
    assert response.status_code == 200


def test_get_comments(client):
    client.post('/api/comments', json={'task_id': 1, 'content': 'First comment'})
    client.post('/api/comments', json={'task_id': 1, 'content': 'Second comment'})
    response = client.get('/api/comments/task/1')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
