from app import app


def test_random_quote_returns_a_quote():
    response = app.test_client().get("/quote")

    assert response.status_code == 200
    assert response.json["quote"]


def test_quotes_returns_three_quotes():
    response = app.test_client().get("/quotes")

    assert response.status_code == 200
    assert len(response.json) == 3


def test_health_returns_up():
    response = app.test_client().get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "UP"}
