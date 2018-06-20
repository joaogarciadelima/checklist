def test_home(client):
    response = client.get('/')
    assert 200 == response.status_code
