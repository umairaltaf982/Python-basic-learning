# The Best Project

## Student Course Management System (Learning Management System - Mini Version)

> Not an LMS like Moodle.

A simple web application where:

- Students register/login
- Teachers register/login
- Teachers create courses
- Students enroll in courses
- Teachers upload assignments
- Students submit assignments
- Teachers grade submissions
- Students see grades
- Admin manages everything

This project is small enough to finish in **2-3 weeks** but covers almost the entire Django ecosystem.

---

## Why this project?

Because it contains almost every important Django concept.

| Django Concept | Covered? |
|---|---|
| Project Structure | ✅ |
| Apps | ✅ |
| Models | ✅ |
| Relationships | ✅ |
| Migrations | ✅ |
| Admin Panel | ✅ |
| URLs | ✅ |
| Views | ✅ |
| Templates | ✅ |
| Static Files | ✅ |
| Media Files | ✅ |
| Forms | ✅ |
| Model Forms | ✅ |
| Authentication | ✅ |
| Login Required | ✅ |
| Sessions | ✅ |
| Messages Framework | ✅ |
| CRUD | ✅ |
| Class Based Views | Later |
| Function Based Views | First |
| Pagination | ✅ |
| Search | ✅ |
| Filtering | ✅ |
| File Upload | ✅ |
| Signals | ✅ |
| Custom User Model | ✅ |
| Permissions | ✅ |
| Query Optimization | ✅ |
| Deployment | Later |

By the end, you'll understand almost all of Django.

---

## Overall Project Structure

```
CourseManagement/

manage.py

CourseManagement/
    settings.py
    urls.py
    wsgi.py
    asgi.py

accounts/
courses/
assignments/
enrollments/
templates/
static/
media/
```

Notice something important:

Instead of putting everything in one app...
We split the project into apps.
Each app has one responsibility.

---

## Apps

### 1. accounts

Handles

- Register
- Login
- Logout
- User Profile
- Teacher
- Student

### 2. courses

Handles

- Course creation
- Course listing
- Course details
- Update
- Delete

### 3. enrollments

Handles

- Student enrolls
- Student leaves course

### 4. assignments

Handles

- Assignment upload
- Assignment submission
- Marks

---

## Folder Structure

```
CourseManagement/

accounts/
    models.py
    views.py
    urls.py
    forms.py
    admin.py
    signals.py

courses/
    models.py
    views.py
    urls.py
    forms.py
    admin.py

assignments/
    models.py
    views.py
    urls.py
    forms.py
    admin.py

enrollments/
    models.py
    views.py
    urls.py
    admin.py

templates/

    base.html

    accounts/
    courses/
    assignments/
    enrollments/

static/

    css/
    js/
    images/

media/
```

This is how real Django projects are organized.

---

## Database Design

### User

**User**

- id
- username
- email
- password
- role
  - (Student / Teacher)

### Course

**Course**

- id
- title
- description
- teacher (FK)
- created_at

### Enrollment

**Enrollment**

- id
- student (FK)
- course (FK)
- enrolled_at

> Many-to-Many relationship through an explicit model.

### Assignment

**Assignment**

- id
- course (FK)
- title
- description
- deadline

### Submission

**Submission**

- id
- assignment (FK)
- student (FK)
- pdf
- marks
- submitted_at

---

## Development Order

> This is the biggest mistake beginners make.
> They randomly create files.
> Instead, follow this order.

### Phase 1

Create Project

```bash
django-admin startproject CourseManagement
```

Understand

- manage.py
- settings.py
- urls.py

Nothing else.

### Phase 2

Create apps

```bash
python manage.py startapp accounts
python manage.py startapp courses
python manage.py startapp enrollments
python manage.py startapp assignments
```

Learn:

- Why apps exist
- App structure
- How apps communicate

### Phase 3

Configure `settings.py`

Add

- INSTALLED_APPS
- Templates
- Static
- Media
- Custom User

### Phase 4

Models

> This is the most important phase.

Create

- accounts/models.py
- courses/models.py
- assignments/models.py
- enrollments/models.py

Do not write views yet.

### Phase 5

Migrations

Understand

- `makemigrations`
- `migrate`
- `showmigrations`
- `sqlmigrate`

These are fundamental.

### Phase 6

Admin

Register models.

Customize

- `list_display`
- `search_fields`
- filters
- ordering

Use Admin to inspect and manage your data.

### Phase 7

URLs

```
Project URLs
    ↓
App URLs
    ↓
Views
```

Understand URL routing before rendering templates.

### Phase 8

Views

Start with Function-Based Views.

Implement:

- Home
- Course List
- Course Detail
- Create Course
- Update Course
- Delete Course

### Phase 9

Templates

Create

- base.html
- navbar.html
- footer.html

Then

- home.html
- course_list.html
- course_detail.html

Understand

- Template inheritance
- Includes
- Variables
- Loops
- Conditions

### Phase 10

Forms

Learn

- `forms.Form`
- `ModelForm`

Understand when to use each.

### Phase 11

Authentication

Implement

- Register
- Login
- Logout
- Password change

Protect views with authentication.

### Phase 12

CRUD

Now implement

- Create
- Read
- Update
- Delete

for every model.

### Phase 13

Search

Course search

Learn query parameters and filtering.

### Phase 14

Pagination

Display

10 courses per page.

### Phase 15

File Upload

Students upload assignment PDFs.

Learn media file handling.

### Phase 16

Permissions

```
Teachers
    ↓
Can create assignments

Students
    ↓
Cannot
```

Implement role-based access.

### Phase 17

Messages

Display

- Course Created
- Login Successful
- Assignment Submitted

using Django's messages framework.

### Phase 18

Signals

Example

When a user is created,
Automatically create a profile.

This introduces Django signals.

### Phase 19

Optimization

Learn

- `select_related()`
- `prefetch_related()`

See how they reduce database queries.

---

## Which files should be written first?

Here's a practical order for each app:

1. `models.py`
2. `admin.py`
3. `forms.py`
4. `urls.py`
5. `views.py`
6. `templates/`
7. `static/`
8. `tests.py` (optional initially)

This keeps your development aligned with Django's request-response flow.

---

## The Request Flow You Should Understand

One of the most important mental models in Django is how a request travels through the application:

```
Browser
    ↓
Project urls.py
    ↓
App urls.py
    ↓
View
    ↓
Model (if data is needed)
    ↓
Database
    ↓
View
    ↓
Template
    ↓
HTML Response
    ↓
Browser
```

As you build the project, always ask yourself where you are in this flow.