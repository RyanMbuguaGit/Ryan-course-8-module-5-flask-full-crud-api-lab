# Event Management API

A simple RESTful API built with Python and Flask that supports full CRUD operations on events. Data is stored in memory (a Python list of `Event` objects), so it resets every time the server restarts.

## Features

- Create a new event with `POST`
- Update an event's title with `PATCH`
- Delete an event with `DELETE`
- List all events with `GET`
- JSON responses using `jsonify()` with clear error messages
- Meaningful HTTP status codes

## Setup

1. Clone the repository and open the project folder.
2. Install Flask:

```bash
pip install flask
```

3. Run the server:

```bash
python app.py
```

The API runs at `http://localhost:5000`.

## Routes

| Method | Route            | Description             | Success Code |
|--------|------------------|-------------------------|--------------|
| GET    | `/events`        | List all events         | 200 OK       |
| POST   | `/events`        | Create a new event      | 201 Created  |
| PATCH  | `/events/<id>`   | Update an event's title | 200 OK       |
| DELETE | `/events/<id>`   | Delete an event         | 204 No Content |

## Example Requests and Responses

### GET /events

Response (200):

```json
[
  { "id": 1, "title": "Tech Meetup" },
  { "id": 2, "title": "Python Workshop" }
]
```

### POST /events

Request body:

```json
{ "title": "Hackathon" }
```

Response (201):

```json
{ "id": 3, "title": "Hackathon" }
```

### PATCH /events/1

Request body:

```json
{ "title": "Hackathon 2025" }
```

Response (200):

```json
{ "id": 1, "title": "Hackathon 2025" }
```

### DELETE /events/2

Response: `204 No Content` (empty body)

## Error Responses

| Status | When it happens                                   | Response body                      |
|--------|---------------------------------------------------|------------------------------------|
| 400    | The `title` is missing from the request body      | `{ "error": "Title is required" }` |
| 404    | No event exists with the given ID                 | `{ "error": "Event not found" }`   |

## Testing the API

You can test the routes with Postman, curl, or PowerShell. Example using PowerShell:

```powershell
# Create an event
Invoke-WebRequest -Method POST -Uri http://localhost:5000/events -ContentType "application/json" -Body '{"title": "Hackathon"}' -UseBasicParsing

# Update an event
Invoke-WebRequest -Method PATCH -Uri http://localhost:5000/events/1 -ContentType "application/json" -Body '{"title": "Hackathon 2025"}' -UseBasicParsing

# Delete an event
Invoke-WebRequest -Method DELETE -Uri http://localhost:5000/events/2 -UseBasicParsing
```

## Design Notes

- Route paths use nouns (`/events`) following RESTful conventions.
- A helper function, `find_event()`, avoids repeating the search-by-ID logic.
- Input is validated before any data is changed.
- Logic is kept modular so a real database can be added later.