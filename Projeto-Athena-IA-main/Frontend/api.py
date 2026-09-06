import os
import httpx

BASE_URL = os.getenv('API_URL', 'http://api:8000')

def _request(method, path, token=None, **kwargs):
    headers = kwargs.pop('headers', {})
    if token:
        headers['Authorization'] = f'Bearer {token}'
    response = httpx.request(method, f'{BASE_URL}{path}', headers=headers, timeout=10, **kwargs)
    response.raise_for_status()
    return response.json() if response.content else None

def login(email, password):
    return _request('POST', '/auth/login', data={'username': email, 'password': password})

def register(email, password):
    return _request('POST', '/auth/register', json={'email': email, 'password': password})
