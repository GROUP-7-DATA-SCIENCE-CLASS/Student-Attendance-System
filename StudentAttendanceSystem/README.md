# Student Attendance Management System

## 1. Project Overview

The **Student Attendance Management System** is a web-based application developed using Python and Django as part of the CSC2105 – Object-Oriented Programming course at Uganda Christian University.

The system is designed to simplify student registration and attendance management by providing an organized platform for storing student information, recording daily attendance and viewing attendance records.

The project demonstrates how Python Object-Oriented Programming concepts can be applied in developing database-driven web applications using Django.

## 2. Project Objectives

- Develop a functional web application using the Django framework.
- Register and manage student information.
- Record daily student attendance.
- Monitor attendance records and statuses.
- Demonstrate the relationship between Django models, databases and Object-Oriented Programming concepts.

## 3. Key Features

### Student Management
- Register new students.
- Store student ID, full name, email address and course.
- View the registered student directory.
- Search and filter student records through Django Admin.

### Attendance Management
- Record student attendance.
- Categorize attendance as Present, Absent or Late.
- View attendance records.
- Filter attendance records by date and status.
- Prevent duplicate attendance records for the same student on the same date.

### Dashboard
- Display the total number of registered students.
- Display the total number of attendance records.
- Provide quick navigation to important application functions.

### Django Administration
- Manage student records.
- Manage attendance records.
- Search and filter database records.
- Perform administrative operations through Django's built-in administration interface.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| Django | Web application framework |
| SQLite | Relational database |
| HTML | Web page structure |
| CSS | Application styling |
| Bootstrap-free custom CSS | Custom interface styling |
| VS Code | Development environment |
| Git and GitHub | Version control and collaboration |

## 5. Project Structure

```text
StudentAttendanceSystem/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── attendance/
│   ├── migrations/
│   ├── templates/
│   │   └── attendance/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── student_list.html
│   │       ├── student_form.html
│   │       ├── attendance_list.html
│   │       └── attendance_form.html
│   │
│   ├── static/
│   │   └── attendance/
│   │       └── style.css
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── venv/                 # Local virtual environment (not committed)
├── db.sqlite3            # Local database (not committed)
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 6. Database Design

The application uses two primary Django models:

**Student**

Stores student information:
- student_id
- full_name
- email
- course
- date_registered

**Attendance**

Stores student attendance information:
- student
- date
- status
- recorded_at

### Relationship Between the Models

The application implements a one-to-many relationship between Student and Attendance.

One student can have multiple attendance records, but each attendance record belongs to one student.

The relationship is implemented using Django's `ForeignKey`.

A unique database constraint on the combination of student and date prevents duplicate attendance entries for the same student on a particular day.

SQLite is used as the default database.

## 7. Object-Oriented Programming Concepts

The project demonstrates the following OOP concepts:

- **Classes and Objects:** Student and Attendance are classes, while individual database records are represented as objects.
- **Inheritance:** Both models inherit from Django's `models.Model` class.
- **Encapsulation:** Models group related attributes and behaviour into structured classes.
- **Abstraction:** Django's Object-Relational Mapper (ORM) simplifies database operations without requiring direct SQL queries for routine operations.
- **Polymorphism:** Both models implement their own `__str__()` methods to provide appropriate string representations of their objects.

## 8. Installation and Setup

Follow these instructions to run the project locally.

### Prerequisites

Ensure that you have installed:

- Python
- Visual Studio Code or another Python IDE
- Git (optional, for cloning the repository)

### Step 1: Clone the Repository

```bash
git clone https://github.com/GROUP-7-DATA-SCIENCE-CLASS/Student-Attendance-System
```

Navigate into the project directory:

```bash
cd StudentAttendanceSystem
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```cmd
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Apply Database Migrations

```bash
python manage.py migrate
```

### Step 6: Create an Administrator Account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your administrator credentials.

### Step 7: Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

**Main Application:**

http://127.0.0.1:8000/

**Django Administration:**

http://127.0.0.1:8000/admin/

## 9. Application URLs

| URL | Functionality |
|---|---|
| `/` | Application dashboard |
| `/students/` | View registered students |
| `/students/register/` | Register a new student |
| `/attendance/` | View attendance records |
| `/attendance/record/` | Record student attendance |
| `/admin/` | Django administration |

## 10. Sample Data

The application should be populated with at least three student records and corresponding attendance records for demonstration purposes.

Sample student records can be created through the application interface or Django Admin.

Each attendance record should be associated with an existing student.

## 11. Collaboration and Version Control

Git and GitHub can be used to support collaborative development.

The following files and folders should not be committed to the repository:

- Virtual environment folders (`venv/`, `.venv/`).
- Local SQLite database (`db.sqlite3`).
- Python cache files (`__pycache__/`).
- Environment variables and secret configuration files.

Migration files should be committed because they describe the database schema and allow other developers to recreate the database structure.

Each group member should create an independent virtual environment and install the dependencies using `requirements.txt`.

## 12. Future Improvements

Potential enhancements include:

- User authentication and role-based access control.
- Student attendance reports.
- Attendance percentage calculations.
- Exporting attendance reports to PDF or Excel.
- Attendance analytics and visualizations.
- Improved form validation and user feedback.

## 13. Academic Information

**Course:** CSC2105 – Object-Oriented Programming Using Python

**Institution:** Uganda Christian University

**Project:** Student Attendance Management System

**Framework:** Django

**Project Type:** Group Practical Assignment – Introduction to Django Web Development

---

*Developed as an academic project to demonstrate the application of Python, Django, database management and Object-Oriented Programming principles in web application development.*