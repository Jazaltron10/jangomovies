# Movie Review API (JWT Edition)

This project is a **Django REST Framework (DRF)** powered application that allows users to submit, view, update, and delete movie reviews. The API supports token-based authentication using **JSON Web Tokens (JWT)** to ensure secure access, and features paginated responses, filtering capabilities, and an extendable user authentication system.

## Key Features

- **JWT Authentication**: Provides secure token-based authentication using JWT (JSON Web Tokens).
- **Review CRUD Operations**: Authenticated users can create, read, update, and delete movie reviews.
- **Pagination**: Paginated response to manage large sets of reviews efficiently (default 5 per page).
- **Filtering**: Easily filter reviews based on different fields using `django_filters`.
- **Security and Best Practices**: Features such as password validators and CSRF protection are enabled to ensure secure operations.
- **Environment Configurations**: Environment variables (`dotenv`) are used to secure sensitive data like secret keys and database credentials.

## Requirements

- Python 3.10+
- Django 5.1
- PostgreSQL or SQLite3 (for development)
- Django REST Framework
- Simple JWT (for token-based authentication)

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/moviereview-jwt.git
cd moviereview-jwt
```

### 2. Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and define your sensitive environment variables:

```bash
SECRET_KEY=your-secret-key
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=your-database-host
DB_PORT=your-database-port
```

> Note: If you want to switch to SQLite for local development, you can use the default settings from the `settings.py` file and skip the database environment variables.

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

To access the Django admin and perform actions as an authenticated user, create a superuser:

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## JWT Authentication

The project uses **JWT** for authenticating users. To obtain a token, send a POST request to the `/auth/` endpoint with your username and password. For example:

```bash
POST /auth/
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

You will receive an `access` and `refresh` token, which you can use to authenticate API requests.

- Access token: Valid for **5 days**
- Refresh token: Valid for **10 days**

### Example: Making Authenticated Requests

After obtaining the JWT, include it in your requests as a `Bearer` token in the header:

```bash
Authorization: Bearer your_access_token
```

## Endpoints

- `/auth/`: Obtain JWT token (POST)
- `/api-auth/login/`: DRF browsable API login page
- `/reviews/`: Movie review operations (GET, POST, PUT, DELETE)

## Security Features

- **JWT Authentication**: Secure token-based authentication using the `rest_framework_simplejwt` package.
- **Password Validation**: Ensures user passwords meet security standards.
- **CSRF Protection**: Enabled by default for enhanced security in form submissions.
- **Whitenoise Middleware**: Used to serve static files securely and efficiently in production environments.

## Deployment

Ensure the following are set for production:

- **DEBUG**: Set to `False` in `settings.py`.
- **SECRET_KEY**: Set a unique secret key using environment variables.
- **ALLOWED_HOSTS**: Update this to include your domain or IP address.

## Database Configuration

The project supports both **PostgreSQL** and **SQLite**:

- **SQLite**: Used by default in local development.
- **PostgreSQL**: For production, you can configure PostgreSQL by updating the `DATABASES` section in `settings.py` and setting up your environment variables for `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, and `DB_PORT`.

## Contributing

Feel free to fork this repository, open issues, and submit pull requests to contribute to the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any queries or suggestions, please reach out to the project maintainers at `jazaltron.jan@gmail.com`.

---
