import requests
import pytest

BASE_URL = "https://yougile.com/api-v2"
API_KEY = ""

HEADERS = {
    "Authorization": f"Token {API_KEY}",
    "Content-Type": "application/json"
}


# Позитивные тесты

def test_create_project():
    valid_project_payload = {'title': 'Test Project'}
    response = requests.post(f"{BASE_URL}/projects", json=valid_project_payload, headers=HEADERS)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


def test_get_all_projects():
    response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert len(response.json()) > 0, "No projects found"


def test_get_project_by_id():
    valid_project_payload = {'title': 'Test Project'}
    create_response = requests.post(f"{BASE_URL}/projects", json=valid_project_payload, headers=HEADERS)
    project_id = create_response.json().get('id')
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_update_project():
    valid_project_payload = {'title': 'Updated Project'}
    create_response = requests.post(f"{BASE_URL}/projects", json=valid_project_payload, headers=HEADERS)
    project_id = create_response.json().get('id')
    updated_payload = {'title': 'Updated Project Name'}
    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=updated_payload, headers=HEADERS)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


# Негативные тесты

def test_create_project_missing_title():
    invalid_payload = {}
    response = requests.post(f"{BASE_URL}/projects", json=invalid_payload, headers=HEADERS)
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"


def test_get_project_by_invalid_id():
    response = requests.get(f"{BASE_URL}/projects/invalid-id", headers=HEADERS)
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"


def test_update_project_with_invalid_id():
    invalid_project_id = 'nonexistent-id'
    updated_payload = {'title': 'Updated Title'}
    response = requests.put(f"{BASE_URL}/projects/{invalid_project_id}", json=updated_payload, headers=HEADERS)
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"


def test_create_project_invalid_title():
    invalid_payload = {'title': 12345}
    response = requests.post(f"{BASE_URL}/projects", json=invalid_payload, headers=HEADERS)
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"