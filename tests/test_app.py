import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Online Quiz Application" in response.data


def test_quiz_page(client):
    response = client.get("/quiz")
    assert response.status_code == 200
    assert b"Online Quiz" in response.data


def test_quiz_submission(client):
    answers = {
        "question_0": "New Delhi",
        "question_1": "HTML",
        "question_2": "Central Processing Unit",
        "question_3": "Docker",
        "question_4": "Git",
        "question_5": "Continuous Integration",
        "question_6": "Guido van Rossum",
        "question_7": "HTTPS",
        "question_8": "Application Programming Interface",
        "question_9": "GitHub"
    }

    response = client.post("/submit", data=answers)

    assert response.status_code == 200
    assert b"10 / 10" in response.data
    assert b"100.0%" in response.data