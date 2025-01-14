
# Tubonge Backend

## Project Objective
The objective of this project is to develop a backend service for a messaging application called "Tubonge". The backend handles user authentication, message storage, and retrieval. The service is built using Django and PostgreSQL.

## Key Features
1. **User Authentication**:
   - Register new users
   - Login existing users
   - JWT-based authentication

2. **Messaging**:
   - Send messages between users
   - Retrieve message history between users

3. **Database**:
   - Use PostgreSQL for data storage
   - Create a database named "tubonge_db"

4. **API Endpoints**:
   - User registration and login endpoints
   - Endpoints for sending and retrieving messages


## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- PostgreSQL
- Django
- Django REST framework
- psycopg2

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/its-coded-coder/tubonge-backend.git
   cd tubonge-backend
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure PostgreSQL**:
   - Create a PostgreSQL database named `tubonge_db`.
   - Create a PostgreSQL user named `tubonge_user` with password `tubonge_password`.
   - Grant all privileges on the `tubonge_db` database to the `tubonge_user`.

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### User Authentication
- **Register**: `POST /auth/register/`
- **Login**: `POST /auth/login/`

### Messaging
- **Send Message**: `POST /messaging/send/`
- **Message History**: `GET /messaging/history/`

## Testing
To run the tests, use the following command:
```bash
python manage.py test
```

## Documentation
API documentation is provided using Swagger. Access the documentation at `/swagger/`.

## License
This project is licensed under the MIT License.
