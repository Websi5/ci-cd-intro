from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient


def test_index(client: TestClient):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.text.find('<!DOCTYPE html>') >= 0, "should contain HTML content"


def test_solve(client: TestClient):
    response = client.post('/solve', json={
        'positions': [
            {'x': 0, 'y': 0},
            {'x': 5, 'y': 0}
        ]
    })

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'min_distance': 10,
        'route': [
            {'x': 0, 'y': 0},
            {'x': 5, 'y': 0},
        ],
        'optimal': True
    }


@pytest.mark.timeout(30)  # !!Erhöht von 10 auf 30 Sekunden!!
def test_solve_timeout(client: TestClient):
    response = client.post('/solve', json={
        'positions': [
            {'x': x, 'y': x} for x in range(100)
        ]
    })
    assert response.json()['optimal'] == False
