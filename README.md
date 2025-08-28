# My Cafe App

A **Flask-based web application** to manage cafes, their locations, and pricing. The app allows users to add new cafes, view all favourite cafes, retrieve a random cafe, search by location, and update cafe pricing. This project uses **SQLite** for data storage and provides both **HTML views** and **JSON API endpoints**.

## Project Overview
This project simulates a cafe directory management system:
- Add new cafes with name, location, and price tier
- Retrieve a random cafe for discovery
- View all cafes in JSON or HTML format
- Search cafes by location
- Update cafe pricing

It’s designed as a simple, real-world web application using Flask (with a mock UI).

## Endpoints
GET /  - Displays the home page.
<img width="876" height="707" alt="mycafe-home" src="https://github.com/user-attachments/assets/63f89927-9053-4036-ab08-aad494c54542" />

GET /add  - Displays a form to add a new cafe.
POST /submit  - Submits the new cafe form and adds it to the database.
<img width="745" height="642" alt="mycafe-add" src="https://github.com/user-attachments/assets/99719be5-7cee-4ebe-a592-48198116766f" />

GET /random  - Returns a random cafe from the database as JSON.

GET /all  - Returns all cafes in JSON format.

GET /all-html  - Returns all cafes rendered in an HTML template.
<img width="1396" height="715" alt="allcafes" src="https://github.com/user-attachments/assets/4c1a8ba1-9988-427f-bfb6-2bfdde5e0cc1" />

GET /search/<location>   - Returns all cafes in a given location as JSON.
<img width="765" height="416" alt="Screenshot 2025-08-28 at 6 24 58 pm" src="https://github.com/user-attachments/assets/e53f7c42-b599-4e3b-9dc6-d3cc06b7922e" />

GET, PATCH  /update-price/<cafe_id>  - Updates the price of a cafe by ID [new_price (as query parameter)]

## Tech Stack
- **Backend Framework:** Flask  
- **Database:** SQLite (`my_cafe.db`)  
- **Language:** Python 3.x  
- **Templating:** Jinja2 (HTML templates)  

## Author
Abi Lt – Full Stack Web Developer
