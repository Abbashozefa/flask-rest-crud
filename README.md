
# # flask-rest-crud
This project is a REST CRUD API created using flask and mongodb.




## Run Locally

Clone the project

```bash
  git clone https://github.com/Abbashozefa/flask-rest-crud.git
```

Go to the project directory

```bash
  cd flask-rest-crud
```

Install dependencies

```bash
  pip install requirements.txt
```

Start the server

```bash
  flask run
```

## Run Docker Image



```bash
  docker pull abbashozefa/flask-crud:latest
```

Run Image

```bash
  docker run -p 5000:5000 abbashozefa/flask-crud
```

## Features

- GET /users - Returns a list of all users.
- GET /users/id - Returns the user with the specified ID.
- POST /users - Creates a new user with the specified data.
- PUT /users/id - Updates the user with the specified ID with the new data.
- DELETE /users/id - Deletes the user with the specified ID.


## Test

Use POSTMAN to test the endpoints
## Screenshots
GET
![Screenshot 2023-07-09 145503](https://github.com/Abbashozefa/flask-rest-crud/assets/72591326/8aa4bda4-7e4f-40dd-b6e5-8949b468fc35)

GET with id
![Screenshot 2023-07-09 145847](https://github.com/Abbashozefa/flask-rest-crud/assets/72591326/df87d1e9-4962-4012-81d9-e184160462b0)

POST
![Screenshot 2023-07-09 145621](https://github.com/Abbashozefa/flask-rest-crud/assets/72591326/be680451-a0fb-4f6b-8b7e-514c6d55b276)

PUT
![Screenshot 2023-07-09 145805](https://github.com/Abbashozefa/flask-rest-crud/assets/72591326/a471e2fb-ff3e-498b-a3cb-66ff777ef0d4)

DELETE
![Screenshot 2023-07-09 145718](https://github.com/Abbashozefa/flask-rest-crud/assets/72591326/11a473af-881c-4ba9-8278-648b737221a9)


## Authors

- [@Abbashozefa](https://github.com/Abbashozefa)

