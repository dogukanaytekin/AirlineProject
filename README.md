This is a Django REST Framework project that provides APIs for managing airplanes, flights, and reservations.
It includes features like flight conflict checking, occupancy checking, unique reservation code generation, and email notifications.

1. Setup Instructions
1.1. Install Python Dependencies
Navigate to the extracted project folder in your terminal and run:
pip install -r requirements.txt
Note: A virtual environment is not mandatory, but recommended for isolated installations.

1.2. Apply Database Migrations
python manage.py migrate

1.3. Create a Superuser (Optional)
python manage.py createsuperuser

1.4. Run the Development Server
python manage.py runserver

API will be available at: http://127.0.0.1:8000/api/

2. API Endpoints
Same list as given in a project pdf given to me.

3. Postman Collection
A postman_collection.json file is included in the project root.
To use it:

Open Postman.
Click Import → Select postman_collection.json.
Test the API endpoints immediately.

4. Features
Flight Conflict Check (1-hour gap rule).

Occupancy Check (no overbooking).

Unique Reservation Code generation.

Email confirmation on reservation creation.

5. Notes
Uses SQLite database.

Requires Python 3.10+ installed on your system.

Email sending is configured via Gmail SMTP. Update credentials in settings.py if needed.
