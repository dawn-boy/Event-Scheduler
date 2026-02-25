# Chronicle --- Event Scheduler

An Event scheduling application built using
**Flask**, **SQLAlchemy**, and **PostgreSQL** (production) with a clean,
typography-focused UI.

Chronicle allows users to create, update, delete, and manage upcoming
events with real-time validation and responsive design.

------------------------------------------------------------------------

## Features

-   Create new events\
-   Update event date/time\
-   Delete events\
-   List upcoming events (sorted)\
-   Prevent past-date creation\
-   RESTful API structure\
-   Production deployment ready (Gunicorn)

------------------------------------------------------------------------

## Tech Stack

### Backend

-   Python 3\
-   Flask\
-   Flask-SQLAlchemy\
-   PostgreSQL (Production)\
-   Gunicorn (WSGI server)

### Frontend

-   HTML5\
-   CSS3 (Responsive design with media queries)\
-   Vanilla JavaScript (Fetch API)

### Deployment

-   Render (Web Service + PostgreSQL)

------------------------------------------------------------------------

## Project Structure
```
event_scheduler/
│
├── app.py
├── models.py
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
└── static/
    ├── styles.css
    └── script.js
```
------------------------------------------------------------------------

## Local Setup
```python
### Clone the repository

git clone https://github.com/yourusername/event_scheduler.git\
cd event_scheduler

### Create virtual environment
python -m venv .venv
source .venv/bin/activate # Linux / Mac

### Install dependencies

pip install -r requirements.txt

### Configure environment variables

Create a `.env` file:

DATABASE_URL=postgresql://username:password@localhost/dbname

### Run the app

python app.py

#Visit: http://127.0.0.1:5000/

```

------------------------------------------------------------------------

## API Endpoints

- GET /events\
- POST /events\
- PUT /events/`<id>`
- DELETE /events/`<id>`

