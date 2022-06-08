from fastapi.testclient import TestClient
from main import app
from hypothesis import given, strategies as st

client = TestClient(app)


def test_greetings_null():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@given(st.text(alphabet=st.characters(whitelist_categories=['L', 'N'])))
def test_greetings_name(name):
    response = client.get("/?name={name}".format(name=name))

    assert response.status_code == 200
    assert response.json() == {"message": "Hello {name}!!!!".format(name=name)}

def test_sum_function():
    response = client.get("/sum?a=5&b=3")

    assert response.status_code == 200
    assert response.json() == {"result": 8}


@given(st.integers(), st.integers())
def test_sum_hypothesis(a, b):
    response = client.get("/sum?a={a}&b={b}".format(a=str(a), b=str(b)))

    assert response.status_code == 200
    assert response.json() == {"result": a + b}
