# Assignmentbetter

This project is a Python-based web application for managing comments, featuring CRUD operations (Create, Read, Update, Delete).

## Features
- RESTful API for comment management
- Modular structure with routes and services
- SQLite database integration

## Project Structure
```
app/
  __init__.py
  app.py
  config.py
  models.py
  routes/
    __init__.py
    comment_routes.py
  services/
    comment_service.py
  instance/
    app.db
```

## API Operations

Below are the main HTTP methods supported by the API:

### POST (Create)

``` 
curl -X POST http://localhost:5000/api/comments -H "Content-Type: application/json" -d "{\"task_id\":1,\"content\":\"Paranji Punith Kumar completed the backend API integration for user authentication\"}"
```
```
curl -X POST http://localhost:5000/api/comments -H "Content-Type: application/json" -d "{\"task_id\":1,\"content\":\"Code reviewed by Paranji Punith Kumar. 10 months of internship experience contributed to efficient implementation\"}"
```
```
curl -X POST http://localhost:5000/api/comments -H "Content-Type: application/json" -d "{\"task_id\":2,\"content\":\"Front-end React component created for task dashboard by Paranji Punith Kumar from IIIT Kottayam\"}"
```

![POST](POST.jpeg)

### GET (Read)
![GET](GET.jpeg)

### PUT (Update)
![PUT](PUT.jpeg)

### DELETE (Delete)
![DELETE](DELETE.jpeg)

## Running the Application
1. Run the app:
   ```bash
   python -m app.app
   ```

## Testing

Run tests using:
```bash
pytest tests/
```

---

Feel free to explore the code and contribute!
