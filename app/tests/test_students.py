def test_create_student(client):
    payload = {
        "name": "Shifa Saqib",
        "reg_no": "2312260",
        "email": "2312260.shifasaqib@gmail.com",
        "course": "DevOps Fundamentals",
    }

    response = client.post("/students", json=payload)

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "Shifa Saqib"
    assert response.json()["reg_no"] == "2312260"


def test_get_students_returns_created_record(client):
    payload = {
        "name": "Shifa Saqib",
        "reg_no": "2312260",
        "email": "2312260.shifasaqib@gmail.com",
        "course": "DevOps Fundamentals",
    }
    client.post("/students", json=payload)

    response = client.get("/students")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["reg_no"] == "2312260"


def test_get_single_student_by_reg_no(client):
    payload = {
        "name": "Shifa Saqib",
        "reg_no": "2312260",
        "email": "2312260.shifasaqib@gmail.com",
        "course": "DevOps Fundamentals",
    }
    client.post("/students", json=payload)

    response = client.get("/students/2312260")

    assert response.status_code == 200
    assert response.json()["name"] == "Shifa Saqib"


def test_get_missing_student_returns_404(client):
    response = client.get("/students/0000000")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"


def test_duplicate_student_returns_400(client):
    payload = {
        "name": "Shifa Saqib",
        "reg_no": "2312260",
        "email": "2312260.shifasaqib@gmail.com",
        "course": "DevOps Fundamentals",
    }

    client.post("/students", json=payload)
    response = client.post("/students", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already exists"
