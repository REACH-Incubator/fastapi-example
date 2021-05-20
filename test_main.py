from fastapi.testclient import TestClient
from main import app
from hypothesis import given, strategies as st

client = TestClient(app)


def test_sum_function():
    response = client.get("/sum?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"result": 8}


@given(st.integers(), st.integers())
def test_sum_hypothesis(a, b):
    response = client.get("/sum?a={a}&b={b}".format(a=str(a), b=str(b)))

    assert response.status_code == 200
    assert response.json() == {"result": a + b}
