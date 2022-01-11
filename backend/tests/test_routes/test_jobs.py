import json

def test_create_job(client,normal_user_token_headers):  
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post("/jobs/create-job/",data=json.dumps(data),headers=normal_user_token_headers)  #added header in the post request
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"


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
    