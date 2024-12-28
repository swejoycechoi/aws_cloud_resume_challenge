import requests
import json

API_URL = "https://0ootsin9k1.execute-api.us-west-1.amazonaws.com/prod/visitor-counter"

# GET Request Test
def test_get_request():
    response = requests.get(API_URL, headers={"Origin": "http://localhost:8080"})
    assert response.status_code == 200
    body = response.json()
    assert "visitor_count" in body
    assert isinstance(body["visitor_count"], int)

'''def test_get_request(mocked_event):
    mocked_event['httpMethod'] = 'GET'
    mocked_event['headers'] = {"Origin": "http://localhost:8080"}
    response = requests.get(API_URL, headers=mocked_event['headers'])
    assert response.status_code == 200
    assert 'visitor_count' in response.json()'''

# POST Invalid Payload Test  
def test_post_invalid_payload():
    # Payload without 'expected_key'
    payload = {"wrong_key": "value"}
    response = requests.post(
        API_URL,
        headers={"Content-Type": "application/json", "Origin": "http://localhost:8080"},
        json=payload,
    )
    assert response.status_code == 400
    body = response.json()
    assert body == {"error": "Invalid payload"}

'''def test_post_invalid_payload(mocked_event):
    mocked_event['httpMethod'] = 'POST'
    mocked_event['headers'] = {"Content-Type": "application/json", "Origin": "http://localhost:8080"}
    mocked_event['body'] = json.dumps({"invalid_key": "invalid_value"})
    response = requests.post(
        API_URL,
        headers=mocked_event['headers'],
        data=mocked_event['body'],
    )
    assert response.status_code == 400'''

# Validate CORS
def test_cors_headers():
    response = requests.get(API_URL, headers={"Origin": "http://localhost:8080"})
    assert response.status_code == 200
    assert response.headers.get("Access-Control-Allow-Origin") == "*"

# Simulate DynamoDB Reset
def test_dynamodb_reset_behavior():
    # Simulate resetting the table
    response = requests.get(API_URL, headers={"Origin": "http://localhost:8080"})
    assert response.status_code == 200
    body = response.json()
    assert "visitor_count" in body
    assert body["visitor_count"] >= 0  # Visitor count should not be negative
    '''visitor_count = response.json().get("visitor_count", -1)
    assert visitor_count >= 0  # Ensures count initializes to 0 or a valid state.'''

# Handle Malformed Payload
def test_malformed_payload():
    payload = '{"invalid_json": true,'  # Malformed JSON
    response = requests.post(
        API_URL,
        headers={"Content-Type": "application/json", "Origin": "http://localhost:8080"},
        data=payload,
    )
    assert response.status_code == 400
    body = response.json()
    assert body == {"error": "Malformed JSON"}

'''def test_malformed_payload():
    payload = '{"invalid_json": true,'  # Malformed JSON
    response = requests.post(
        API_URL,
        headers={"Content-Type": "application/json", "Origin": "http://localhost:8080"},
        data=payload,
    )
    assert response.status_code == 400  # Ensure proper error handling for malformed data.'''