from flask import Blueprint, request, jsonify
from datetime import datetime
from models import Event
from extensions import db

main = Blueprint("main", __name__)

#Create event
@main.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    title = data.get("title")
    description = data.get("description")
    event_date_str = data.get("event_date")

    if not title or not event_date_str:
        return jsonify({"error": "Title and Event Date is required."}), 400
    
    try:
        event_date = datetime.fromisoformat(event_date_str)
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400
    
    if event_date < datetime.now():
        return jsonify({"error": "Cannot create event in the past."}), 400
    
    new_event = Event(
        title=title,
        description=description,
        event_date=event_date
    )

    db.session.add(new_event)
    db.session.commit()

    return jsonify({"message": "Event created"}), 201

@main.route("/")
def home():
    return jsonify({"message": "Hello"}), 201