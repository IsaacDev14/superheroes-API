# Superheroes API

A RESTful Flask API built for managing superheroes and their powers. Built with Flask-RESTful, SQLAlchemy, and Alembic.

## Features

- View a list of heroes and their super names
- View detailed hero profiles including powers and strength level
- View and update power descriptions
- Assign powers to heroes with strength ratings (Strong, Average, Weak)
- Validation errors and clean JSON responses

## Technologies Used

- Python 3.10+
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate (Alembic)
- SQLite (for development)
- Postman (for testing endpoints)

## Project Structure

```
.
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── seed.py
│   └── routes/
│       ├── hero.py
│       ├── power.py
│       └── hero_power.py
├── migrations/
├── instance/             # SQLite database goes here
│   └── app.db            # (created after running migrations)
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-private-repo-url>
cd <project-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize and Run Migrations

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

 The database will be created at `instance/app.db`. Make sure the `instance/` directory exists or is created automatically.

### 5. Seed the Database

```bash
python app/seed.py
```

### 6. Run the Server

```bash
python run.py
```

##  API Endpoints

### GET /heroes

Returns all heroes.

### GET /heroes/<id>

Returns a single hero with nested powers.

### GET /powers

Returns all powers.

### GET /powers/<id>

Returns a single power.

### PATCH /powers/<id>

Updates a power’s description (minimum 20 characters).

### POST /hero_powers

Assigns a power to a hero. Requires:
```json
{
  "strength": "Strong",
  "power_id": 1,
  "hero_id": 3
}
```

##  Validations

- Power description must be at least 20 characters.
- HeroPower strength must be "Strong", "Average", or "Weak".

## Postman Collection

Import the provided Postman collection for testing the API.

## Author

Isaac Mwiti Kubai

---

** Linces **
This project is for learning puporses 
