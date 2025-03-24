# Keywordio-AB
created Django project for libraray management system

A Library Management System built using Django and MySQL (XAMPP). This project allows an admin to manage books (CRUD operations) and enables students to view available books.

Setup & steps to Run Project:
1)Install Requirements
  pip install django mysqlclient

2)Configure Database
  Start XAMPP and enable MySQL
  Create database library_db in phpMyAdmin

3)Update Settings
  # settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'library_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
5) Create Superuser (Optional)
  python manage.py createsuperuser

6) Run Development Server
  python manage.py runserver

7) Access URLs
   Public view: http://127.0.0.1:8000/
  Admin panel: http://127.0.0.1:8000/admin/
  Add books: http://127.0.0.1:8000/add_book/ (after login)






🚀 Features
✅ Admin Functionalities
Signup & Login (with unique email validation)
Manage Books (Add, Update, Delete)
View all books
✅ Student Functionalities
View all books available in the library

🛠️ Technologies Used
Backend: Django (Python)
Database: MySQL (XAMPP)
Frontend: HTML, CSS, Bootstrap

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repository.git
cd your-repository

2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Database
Start XAMPP and enable MySQL
Create a database library_db in phpMyAdmin

5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

6️⃣ Create Superuser (Admin Login)
python manage.py createsuperuser
Enter email, username, and password for admin login.

7️⃣ Run the Project
python manage.py runserver or Open http://127.0.0.1:8000/ in your browser.

📌 Project Structure
Library_Management/
│-- library_management/
│   ├── settings.py
│   ├── urls.py
│   ├── models.py
│   ├── views.py
│-- templates/
│   ├── base.html
│   ├── signup.html
│   ├── login.html
│   ├── book_list.html
│-- static/
│-- README.md

Backend Architecture
Core Components
1)Authentication System

Secure admin authentication using session-based validation
Password hashing via Django's make_password and check_password
Unique email enforcement at model and view levels
Session timeout control (configurable in settings)

2)Database Layer

MySQL relational database (via Django ORM)
Optimized model design with constraints:

3)Business Logic

CRUD operations with atomic transactions
Inventory management (quantity tracking)
Admin privilege escalation prevention

Security Implementation
Feature	                  Implementation Details
CSRF                      Protection	Django Middleware + template {% csrf_token %}
SQL                       Injection Prevention	Django ORM parameterized queries
XSS                       Protection	Automatic template escaping
Session                   Security	SESSION_COOKIE_HTTPONLY = True
Password                  Security	PBKDF2 hashing with SHA-256

API Flow
sequenceDiagram
    Public User->>View: Access /view_books/
    View->>Database: SELECT * FROM books
    Database-->>View: Return book list
    View-->>Public User: Render template (no CRUD buttons)

    Admin->>View: POST /admin_login/
    View->>Database: Verify credentials
    Database-->>View: Return admin record
    View->>Session: Store admin_id
    View-->>Admin: Redirect to dashboard

    Admin->>View: POST /add_book/
    View->>Session: Validate admin_id
    View->>Database: INSERT new book
    Database-->>View: Confirm creation
    View-->>Admin: Redirect with success message


This architecture provides a secure, maintainable foundation that can scale to:

The system adheres to Django best practices while implementing custom security measures appropriate for library management systems.
    
