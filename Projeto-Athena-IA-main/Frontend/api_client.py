import os
import httpx

API_URL = os.getenv("API_URL", "http://localhost:8000")

def request(method, path, token=None, **kwargs):
    headers = {}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    response = httpx.request(method, f"{API_URL}{path}", headers=headers, timeout=10, **kwargs)
    response.raise_for_status()
    return response.json() if response.content else None

def register(name, email, password):
    return request("POST", "/auth/register", json={"name": name, "email": email, "password": password})

def login(email, password):
    return request("POST", "/auth/login", json={"email": email, "password": password})

def me(token):
    return request("GET", "/users/me", token=token)

def tasks(token):
    return request("GET", "/tasks/", token=token)

def create_task(token, title, description, priority):
    return request("POST", "/tasks/", token=token, json={"title": title, "description": description or None, "priority": priority})

def update_task(token, task_id, **data):
    return request("PATCH", f"/tasks/{task_id}", token=token, json=data)

def delete_task(token, task_id):
    return request("DELETE", f"/tasks/{task_id}", token=token)

def routines(token):
    return request("GET", "/routines/", token=token)

def create_routine(token, title, description, duration_minutes):
    return request("POST", "/routines/", token=token, json={"title": title, "description": description or None, "duration_minutes": duration_minutes or None})

def diary(token):
    return request("GET", "/diary/", token=token)

def create_diary(token, content):
    return request("POST", "/diary/", token=token, json={"content": content})
