from fastapi.testclient import TestClient

from src.app import app
from src.app import get_item
from src.functional import calculation

client = TestClient(app)


def test_summation():
    response = client.get("/2+2")
    assert response.status_code == 200
    assert response.json() == 4
    assert get_item("-10+8") == -2
    assert calculation("5+19") == 24


def test_multiply():
    response = client.get("/8*8")
    assert response.status_code == 200
    assert response.json() == 64
    assert get_item("0.5*2") == 1
    assert calculation("1*2") == 2


def test_subtraction():
    response = client.get("/29-28")
    assert response.status_code == 200
    assert response.json() == 1
    assert get_item("-7-10") == -17
    assert calculation("5-6") == -1


def test_divide():
    response = client.get("/40div8")
    assert response.status_code == 200
    assert response.json() == 5
    assert get_item("36div6") == 6
    assert calculation("15div2") == 7.5
