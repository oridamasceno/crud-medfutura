# CRUD MedFutura API

This project is a RESTful API for managing a system that handles the creation, retrieval, updating, and deletion of user records. The API is built using FastAPI and connects to an MS SQL Server database.

## Features
- **Create:** Add new user records to the database.
- **Read:** Retrieve individual or multiple user records.
- **Update:** Modify existing user information.
- **Delete:** Remove user records from the database.

## Endpoints
- **POST /pessoas:** Create a new user record.
- **GET /pessoas/{id}:** Retrieve a specific user by ID.
- **GET /pessoas:** Search for users by name or other criteria.
- **PUT /pessoas/{id}:** Update a user's information.
- **DELETE /pessoas/{id}:** Delete a user by ID.

### Setup Instructions

#### 1. Clone the repository:
```
git clone https://github.com/oridamasceno/crud-medfutura.git
cd crud-medfutura
```

#### 2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

#### 3. Install dependencies:
```
pip install -r requirements.txt
```

#### 4. Configure the database:
- Ensure your MS SQL Server is running and accessible.
- Update the database.py file with your connection details.

#### 5. Run the application:
```
uvicorn main:app --reload
```

#### 6. Access the API documentation:
- Navigate to http://127.0.0.1:8000/docs to explore the API using the interactive Swagger UI.

## Usage

To interact with the API, you can use tools like Postman or curl commands in the terminal. The available endpoints allow you to perform CRUD operations on the user records.
