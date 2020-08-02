import json

import pytest

from app.api import crud
import datetime

def test_create_customer(test_app, monkeypatch):
    test_request_payload = {
        "customer_code" : "vcr10001",
        "gender" : "male",
        "birthday" : "18/08/1999",
        "district" : "Q. Tan Binh",
        "city" : "Ho Chi Minh",
        "email" : "haha@gmail.com",
        "first_purchase_date" : '2032-04-23T10:20:30.400+02:30'
    }
    test_response_payload = {
        "id": 1,
        "customer_code" : "vcr10001",
        "gender" : "male",
        "birthday" : "18/08/1999",
        "district" : "Q. Tan Binh",
        "city" : "Ho Chi Minh",
        "email" : "haha@gmail.com",
        "first_purchase_date" : '2032-04-23T10:20:30.400+02:30'
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, "insert_customer", mock_post)

    response = test_app.post("/customer/", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload