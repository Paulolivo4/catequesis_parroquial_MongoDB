# Catequesis Parroquial (Flask + MongoDB)

Web app to manage the catechized users ("catequizados") of a parish. It supports registering, listing, searching, editing and deleting records, stored in **MongoDB**.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)

> This is the MongoDB phase of a university project. The earlier SQL Server version is [BDD_Kp_InterfazWeb_Py](https://github.com/Paulolivo4/BDD_Kp_InterfazWeb_Py).

## Features

- Register a catequizado with name, surname, birth date, ID number, address, phone, email, parish and group.
- Search, edit and delete records by ID.
- Required-field validation on the registration form, with flash messages for success and errors.

## Tech stack

Python · Flask 2.2 · Flask-PyMongo · Jinja2 templates · MongoDB (collection `catequizados`).

## Project structure

```
flask-mongodb-app/
├── run.py                 # Entry point
├── config.py              # SECRET_KEY / MONGO_URI settings
├── requirements.txt
└── app/
    ├── __init__.py        # create_app(), blueprint registration
    ├── db.py              # PyMongo initialization
    ├── routes.py          # Registration, search, edit, delete
    └── templates/         # index, registro, buscar, editar, eliminar
```

## Getting started

**Requirements:** Python 3.10+ and a MongoDB instance (local or Atlas).

```bash
cd flask-mongodb-app
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

Open <http://127.0.0.1:5000/>.

## Configuration

Settings are read from environment variables (see `flask-mongodb-app/.env.example`):

| Variable | Purpose | Default |
| --- | --- | --- |
| `MONGO_URI` | MongoDB connection string | `mongodb://localhost:27017/catequesis_parroquial` |
| `SECRET_KEY` | Flask session/flash key | random per start |

## Routes

| Route | Purpose |
| --- | --- |
| `/` | List all catequizados |
| `/registro_catequizado` | Register a new record |
| `/buscar_catequizado` | Search |
| `/editar_catequizado`, `/actualizar_catequizado` | Edit and update |
| `/eliminar_catequizado` | Delete by ID |

## Roadmap

- [ ] Remove the unused sample models and the `/add` and `/delete` routes
- [ ] Tests
