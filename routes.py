from flask import Blueprint, request, jsonify, render_template
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

@main.route('/events', methods=['GET'])
def list_events():
    events = Event.query.filter(Event.event_date >= datetime.now()) \
                        .order_by(Event.event_date.asc()).all()

    result = []
    for event in events:
        result.append({
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "event_date": event.event_date.isoformat()
        })

    return jsonify(result)


@main.route("/")
def home():
    return render_template("index.html")

@main.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = Event.query.get(event_id)

    if not event:
        return jsonify({"error": "Event not found"}), 404

    db.session.delete(event)
    db.session.commit()

    return jsonify({"message": "Event deleted"})

@main.route("/events/<int:event_id>", methods=["PUT"])
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    data = request.get_json()

    if "title" in data:
        event.title = data["title"]

    if "event_date" in data:
        event.event_date = datetime.fromisoformat(data["event_date"])

    if "description" in data:
        event.description = data["description"]

    db.session.commit()

    return jsonify({"message": "Event updated successfully"})