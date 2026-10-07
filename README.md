# CareerHub – Job Portal

CareerHub is a Django-based job portal that connects job seekers with employers.

Job seekers can create profiles, search and apply for jobs, and track their applications. Employers can create company profiles, post and manage jobs, and review and update applicant statuses.

The project also includes REST APIs with JWT authentication and role-based permissions.

## Features

### Job Seeker

* User registration and login
* Create and edit job seeker profile
* Upload profile picture
* Add skills, education, experience, GitHub, and LinkedIn
* Browse available jobs
* Search and filter jobs
* Apply for jobs with a resume and cover letter
* View submitted applications
* Track application status
* Job seeker dashboard
* Change password
* Forgot/reset password through email

### Employer

* Employer registration and login
* Create and edit company profile
* Upload company logo
* Post jobs
* View, edit, and delete own jobs
* View applications for posted jobs
* View individual applicant details
* Update application status and add employer notes
* Employer dashboard

### REST API

* Job listing and creation API
* Job detail, update, and delete API
* Job application API
* My applications API
* Employer applications API
* Application detail API
* Application status update API
* JWT access and refresh tokens
* Role-based API permissions
* Job ownership protection
* Application ownership protection

## Technologies Used

* **Python 3.12**
* **Django 6.0.7**
* **Django REST Framework**
* **Simple JWT**
* **SQLite**
* **HTML5**
* **CSS3**
* **Bootstrap**
* **Gmail SMTP**
* **Git & GitHub**

## API Documentation

CareerHub provides REST APIs for job and application management.

### JWT Authentication

| Endpoint              | Method | Description                          |
| --------------------- | ------ | ------------------------------------ |
| `/api/token/`         | POST   | Obtain JWT access and refresh tokens |
| `/api/token/refresh/` | POST   | Refresh an access token              |

### Job APIs

| Endpoint          | Method | Description            |
| ----------------- | ------ | ---------------------- |
| `/api/jobs/`      | GET    | List available jobs    |
| `/api/jobs/`      | POST   | Create a new job       |
| `/api/jobs/<id>/` | GET    | View job details       |
| `/api/jobs/<id>/` | PUT    | Update a job           |
| `/api/jobs/<id>/` | PATCH  | Partially update a job |
| `/api/jobs/<id>/` | DELETE | Delete a job           |

### Application APIs

| Endpoint                       | Method | Description                                |
| ------------------------------ | ------ | ------------------------------------------ |
| `/api/apply/<id>/`             | POST   | Apply for a job                            |
| `/api/my-applications/`        | GET    | View the current job seeker's applications |
| `/api/employer-applications/`  | GET    | View applications for the employer's jobs  |
| `/api/app-detail/<id>/`        | GET    | View application details                   |
| `/api/app-status-update/<id>/` | PATCH  | Update application status                  |

### API Security

* JWT authentication is used for API access.
* Job seekers and employers have different API permissions.
* Employers can modify only their own jobs.
* Employers can access only applications submitted to their own jobs.
* Job seekers can apply for jobs and view their own applications.
* Duplicate applications are prevented.


Project Highlights
Built a complete job portal using Django
Implemented separate workflows for job seekers and employers
Developed job posting, searching, filtering, and application management
Implemented REST APIs using Django REST Framework
Added JWT authentication for APIs
Implemented role-based permissions and ownership checks
Added password change and email-based password reset
Configured Gmail SMTP for password reset emails
Used environment variables to protect sensitive configuration
Designed responsive pages using Bootstrap
Managed the project using Git and GitHub