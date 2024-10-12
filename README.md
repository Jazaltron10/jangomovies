# **Movie Review API**

## **Project Overview**
The **Movie Review API** allows users to create, read, update, and delete movie reviews. Users can also view reviews by movie and search/filter reviews by rating. The API is built using Django and Django REST Framework, providing a secure, RESTful API that interacts with a database to store user-generated reviews.

## **Features**
- **User Authentication**: Users can register, log in, and manage their profiles.
- **Review Management**: Authenticated users can create, update, and delete reviews.
- **Movie Reviews**: Users can view reviews for a specific movie.
- **Search and Filter**: Search for reviews by movie title or filter by rating.
- **Pagination**: Supports pagination for large datasets of reviews.

## **Technologies Used**
- **Python 3.x**: Main programming language.
- **Django**: Web framework for handling backend logic.
- **Django REST Framework (DRF)**: Framework for building RESTful APIs.
- **PostgreSQL/SQLite**: Database for storing user and review data.
- **JWT Authentication (Optional)**: Token-based authentication for securing API endpoints.
- **Heroku/PythonAnywhere**: For deployment.

---

## **API Endpoints**

### **Authentication**
- **POST** `/api/auth/register/` - Register a new user.
- **POST** `/api/auth/login/` - Log in a user and get a token (if using JWT).
- **POST** `/api/auth/logout/` - Log out a user (if using JWT).

### **Reviews**
- **GET** `/api/reviews/` - List all reviews (supports filtering and pagination).
- **POST** `/api/reviews/` - Create a new review (authenticated users only).
- **GET** `/api/reviews/<review_id>/` - Retrieve details for a specific review.
- **PUT/PATCH** `/api/reviews/<review_id>/` - Update a review (authenticated users only).
- **DELETE** `/api/reviews/<review_id>/` - Delete a review (authenticated users only).

### **Movies**
- **GET** `/api/movies/<movie_title>/reviews/` - List all reviews for a specific movie (with sorting and pagination).

### **Filtering & Searching**
- **GET** `/api/reviews/?movie_title=<title>` - Search reviews by movie title.
- **GET** `/api/reviews/?rating=<value>` - Filter reviews by rating (e.g., 4-star reviews).

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/movie-review-api.git
cd movie-review-api
```

### **2. Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate    # On Windows, use venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**
Create a `.env` file in the root directory and add the following:

```bash
SECRET_KEY=your_django_secret_key
DEBUG=True  # For development
DATABASE_URL=your_database_url  # Use SQLite for local dev or PostgreSQL for production
```

### **5. Apply Migrations**
```bash
python manage.py migrate
```

### **6. Create a Superuser (Optional)**
```bash
python manage.py createsuperuser
```

### **7. Run the Development Server**
```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`.

---

## **Running Tests**
To run the tests for the API, use the following command:

```bash
python manage.py test
```

---

## **Deployment**
### **Deploy to Heroku**
1. **Install Heroku CLI**: If you haven't installed it yet, follow [this guide](https://devcenter.heroku.com/articles/heroku-cli).
2. **Create a Heroku App**:
   ```bash
   heroku create your-app-name
   ```
3. **Set up environment variables** on Heroku:
   ```bash
   heroku config:set SECRET_KEY=your_django_secret_key
   heroku config:set DEBUG=False
   ```
4. **Push code to Heroku**:
   ```bash
   git push heroku main
   ```

For more detailed instructions, refer to the [Heroku Deployment Guide](https://devcenter.heroku.com/articles/deploying-python).

---

## **Project Report**
Refer to the project report [here](link-to-your-google-doc).

---

## **Future Enhancements**
- **Third-party API Integration**: Fetch movie details from OMDB or TMDB.
- **User Likes**: Implement a feature where users can "like" reviews.
- **Review Comments**: Allow users to comment on each other's reviews.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contributing**
Feel free to submit issues or pull requests if you would like to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

---

## **Contact**
For any questions or suggestions, feel free to reach out:
- **Email**: jazaltron.jan@gmail.com
- **GitHub**: [Jazaltron10](https://github.com/Jazaltron10/movie_review_api)

---

This `README.md` file gives a comprehensive overview of your **Movie Review API** project, providing clear instructions and details on how to use the API, set it up, and contribute.