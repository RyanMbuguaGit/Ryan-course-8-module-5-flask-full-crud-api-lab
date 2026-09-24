from flask import Flask, jsonify, request

app = Flask(__name__)


# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]


# Helper function: find an event by its ID (avoids repeating this search)
def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None


# GET /events - list all events (handy for testing in the browser)
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify([event.to_dict() for event in events]), 200


# POST /events - Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    data = request.get_json(silent=True)

    # Validate: body must exist and contain a title
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Generate the next ID (highest existing ID + 1)
    new_id = max((event.id for event in events), default=0) + 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


# PATCH /events/<id> - Update the title of an event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    event = find_event(event_id)

    # 404 if the event doesn't exist
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json(silent=True)

    # 400 if title is missing
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    event.title = data["title"]
    return jsonify(event.to_dict()), 200


# DELETE /events/<id> - Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = find_event(event_id)

    # 404 if the event doesn't exist
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    events.remove(event)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)