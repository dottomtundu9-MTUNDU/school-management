

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
FULL STRUCTURE PROJ
smart-school-ERP/
│
├── backend/                         # FastAPI Backend
│   │
│   ├── app/
│   │   ├── main.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── database.py
│   │   │   ├── security.py
│   │   │   └── dependencies.py
│   │   │
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── auth.py
│   │   │       ├── students.py
│   │   │       ├── teachers.py
│   │   │       ├── finance.py
│   │   │       └── reports.py
│   │   │
│   │   ├── models/
│   │   │   ├── user.py
│   │   │   ├── student.py
│   │   │   ├── teacher.py
│   │   │   ├── academic.py
│   │   │   └── finance.py
│   │   │
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── repositories/
│   │   ├── utils/
│   │   └── middleware/
│   │
│   ├── alembic/
│   ├── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
│
│
├── frontend/                        # React + TypeScript
│   │
│   ├── public/
│   │
│   ├── src/
│   │   │
│   │   ├── app/
│   │   │   ├── router.tsx
│   │   │   ├── providers.tsx
│   │   │   └── store.ts
│   │   │
│   │   ├── components/
│   │   │   ├── ui/
│   │   │   ├── layout/
│   │   │   ├── charts/
│   │   │   └── common/
│   │   │
│   │   ├── features/
│   │   │   │
│   │   │   ├── auth/
│   │   │   ├── dashboard/
│   │   │   ├── students/
│   │   │   ├── teachers/
│   │   │   ├── academics/
│   │   │   ├── attendance/
│   │   │   ├── examinations/
│   │   │   ├── finance/
│   │   │   ├── reports/
│   │   │   └── notifications/
│   │   │
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   └── axios.ts
│   │   │
│   │   ├── hooks/
│   │   ├── types/
│   │   ├── utils/
│   │   ├── styles/
│   │   │
│   │   ├── App.tsx
│   │   └── main.tsx
│   │
│   ├── package.json
│   ├── vite.config.ts
│   └── Dockerfile
│
│
├── database/
│   ├── migrations/
│   └── seeds/
│
├── docker-compose.yml
│
├── docs/
│   ├── API.md
│   ├── DATABASE.md
│   └── ARCHITECTURE.md
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   │
│   ├── workflows/
│   │   └── ci.yml
│   │
│   └── PULL_REQUEST_TEMPLATE.md
│
├── README.md
├── LICENSE
└── .gitignore

REQUIREMENTS
# ==============================
# FastAPI Core
# ==============================
fastapi==0.115.6
uvicorn[standard]==0.34.0


# ==============================
# Database
# ==============================
sqlalchemy==2.0.36
alembic==1.14.0
psycopg2-binary==2.9.10


# ==============================
# Data Validation & Settings
# ==============================
pydantic==2.10.4
pydantic-settings==2.7.0


# ==============================
# Authentication & Security
# ==============================
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.20


# ==============================
# Environment Management
# ==============================
python-dotenv==1.0.1


# ==============================
# Email Services
# ==============================
email-validator==2.2.0


# ==============================
# Background Tasks & Cache
# ==============================
redis==5.2.1
celery==5.4.0


# ==============================
# File Handling & Reports
# ==============================
openpyxl==3.1.5
pandas==2.2.3
reportlab==4.2.5


# ==============================
# API Utilities
# ==============================
fastapi-limiter==0.1.6
python-dateutil==2.9.0.post0


# ==============================
# Logging
# ==============================
loguru==0.7.3


# ==============================
# Testing
# ==============================
pytest==8.3.4
pytest-asyncio==0.25.0
httpx==0.28.1


# ==============================
# Production Server
# ==============================
gunicorn==23.0.0


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
