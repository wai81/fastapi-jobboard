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


def test_retreive_job_by_id(client):
    data = {
        "title": "SDE 1",
        "company": "test company",
        "company_url": "www.company.com",
        "location": "UK, London",
        "description": "Testing",
        "date_posted": "2022-01-05"
        }
    
    client.post("/jobs/create-job", json.dumps(data))
    response = client.get("/job/get/1")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1"
    