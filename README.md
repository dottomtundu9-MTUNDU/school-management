

# 🎓 Smart School ERP API

A modern, scalable, and enterprise-grade School Management System built with FastAPI, PostgreSQL, SQLAlchemy, Alembic, and JWT Authentication.

The platform centralizes student management, academics, attendance, examinations, finance, reporting, and communication into a single secure API.

---

## 🚀 Vision

Smart School ERP aims to digitize and automate school operations while providing a secure, scalable, and maintainable platform for educational institutions.

Target Institutions:

- Primary Schools
- Secondary Schools
- Colleges
- Universities
- Training Institutes

---

## ✨ Features

### Authentication & Authorization

- JWT Authentication
- Refresh Tokens
- User Registration & Login
- Role-Based Access Control (RBAC)
- User Profile Management
- Audit Logging

### Student Management

- Student Registration
- Student Profiles
- Parent/Guardian Assignment
- Student Promotion
- Student Transfer
- Student Documents
- Discipline Records

### Teacher Management

- Teacher Profiles
- Subject Assignment
- Class Assignment
- Attendance Tracking
- Leave Management

### Academic Management

- Academic Years
- Terms / Semesters
- Classes
- Streams
- Subjects
- Timetables

### Attendance Management

- Student Attendance
- Teacher Attendance
- Attendance Reports
- Attendance Analytics

### Examination Management

- Exam Creation
- Marks Entry
- Automated Grading
- GPA Calculation
- Student Ranking
- Report Card Generation

### Finance Management

- Fee Structures
- Invoice Generation
- Payment Processing
- Financial Ledger
- Student Statements
- Defaulters Tracking
- Scholarships & Discounts

### Reporting System

- Academic Reports
- Attendance Reports
- Finance Reports
- Student Reports

Export Formats:

- PDF
- Excel
- CSV

### Communication

- SMS Notifications
- Email Notifications
- School Announcements
- Event Management

### Dashboard Analytics

- Student Statistics
- Teacher Statistics
- Revenue Analytics
- Attendance Analytics
- Academic Performance Analytics

---

## 🏗 Architecture

```text
Client Applications
│
├── Web Dashboard
├── Mobile Application
└── Third Party Integrations
        │
        ▼
FastAPI REST API
        │
        ▼
Business Services Layer
        │
        ▼
SQLAlchemy ORM
        │
        ▼
PostgreSQL Database
```

---

## 📂 Project Structure

```text
smart-school-ERP-API/
│
├── backend/
│   │
│   ├── app/
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   ├── security.py
│   │   │   └── dependencies.py
│   │   │
│   │   ├── models/
│   │   ├── schemes/
│   │   ├── services/
│   │   ├── routers/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── tests/
│   ├── alembic/
│   └── requirements.txt
│
├── frontend/
│
├── docs/
│
└── README.md
```
## 🗄 Core Modules

### User Management

- Users
- Roles
- Permissions
- Refresh Tokens
- Audit Logs

### Student Management

- Students
- Guardians
- Student Documents
- Student Promotions
- Student Transfers

### Teacher Management

- Teachers
- Teacher Subjects
- Teacher Classes
- Teacher Attendance

### Academic Management

- Academic Years
- Terms
- Classes
- Streams
- Subjects
- Timetables

### Attendance

- Student Attendance
- Teacher Attendance

### Examination

- Exams
- Marks
- Grades
- Report Cards

### Finance

- Fee Structures
- Invoices
- Payments
- Ledger Entries
- Scholarships
- Discounts

---

## 🔐 User Roles

### Super Admin
Full system access.

### Admin
School administration management.

### Accountant
Finance and accounting operations.

### Teacher
Academic and classroom management.

### Parent
Student monitoring and fee tracking.

### Student
Academic records and personal information.

---

## 🌐 API Endpoints

```http
/auth
/users

/students
/teachers
/parents

/classes
/subjects
/timetables

/attendance

/exams
/results

/finance

/reports

/dashboard

/notifications
```

---

## ⚙ Technology Stack

### Backend

- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic

### Authentication

- JWT
- OAuth2

### Testing

- Pytest

### Documentation

- Swagger UI
- ReDoc

### DevOps

- Docker
- Docker Compose
- GitHub Actions

---

## 📈 Development Roadmap

### Phase 1

- Authentication
- User Management
- Student Management

### Phase 2

- Teacher Management
- Academic Management
- Attendance

### Phase 3

- Examination & Results

### Phase 4

- Finance & Accounting

### Phase 5

- Dashboard & Reporting

### Phase 6

- Notifications
- Library
- Hostel
- Transport

---

## 🤝 Contributing

Contributions are welcome.

### Workflow

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "Feat: Add new feature"
```

4. Push changes

```bash
git push origin feature/my-feature
```

5. Open a Pull Request

---

## 🧪 Local Development

Clone repository:

```bash
git clone https://github.com/dottomtundu9-MTUNDU/smart-school-ERP-API.git
```

Navigate into backend:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
alembic upgrade head
```

Start development server:

```bash
uvicorn app.main:app --reload
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## 📝 License

This project is licensed under the MIT License.

---

## 👨‍💻 Maintainer

**Dotto Mtundu Hamis**

Backend Developer | FastAPI Developer | Open Source Contributor

---

### ⭐ Support The Project

If you find this project useful, please consider giving it a star on GitHub.
