#!/usr/bin/env python

import pytest
import sys
from pathlib import Path

# get repo top-level directory
tld = Path(__file__).resolve().parents[2]

# add app from `tld / app / app.py`
sys.path.append(str(tld / "app"))

# add models from `tld / app / models`
sys.path.append(str(tld / "app" / "models"))

# add config_public from `tld / config_public.py`
sys.path.append(str(tld / "config_public.py"))

from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_pygments_css(client):
    response = client.get('/pygments.css')
    assert response.status_code == 200

def test_index_extend(client):
    response = client.get('/index/1.html')
    assert response.status_code == 200

def test_staticpage(client):
    response = client.get('/nonexistent/')
    assert response.status_code == 404

def test_tag(client):
    response = client.get('/tag/nonexistent/')
    assert response.status_code == 200
    assert b"List of stuff tagged <em>nonexistent</em>" in response.data
