import json

def test_create_job(client):
    data = {
        "title": "SDE 1",
        "company": "test company",
        "company_url": "www.company.com",
        "location": "UK, London",
        "description": "Testing",
        "date_posted": "2022-01-05"
        }
    
    response = client.post("/jobs/create-job", json.dumps(data))
    
    assert response.status_code == 200