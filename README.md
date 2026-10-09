# Vaccination Scheduling Application

A web-based application designed to streamline the process of scheduling vaccination appointments. This system allows users to register, view available vaccination centers and campaigns, and book appointments, while providing administrators with tools to manage vaccines, centers, and user data.

## 📋 Overview

The Vaccination Scheduling Application is a Django-based web project that addresses the need for an organized and efficient vaccination management system. It provides a clear interface for both end-users (patients) and administrators, handling everything from user authentication to appointment scheduling and campaign management.

## ✨ Key Features

Based on the application's modular structure, the system includes the following core functionalities:

- **User Management & Authentication**: Secure user registration, login, and profile management with email notifications and signals for user-related events.
- **Vaccine & Center Management**: Administrators can manage a catalog of vaccines and a list of vaccination centers, including storage and generic view handling for these entities.
- **Campaign Management**: The system supports the creation and management of vaccination campaigns, allowing for targeted scheduling drives.
- **Appointment Scheduling**: The core `vaccination` module handles the logic for booking and managing vaccination appointments.
- **Custom Admin Interface**: An enhanced Django admin site is configured for efficient backend management and customization of all models.

## 🛠️ Tech Stack

The application is built primarily with Python and the Django framework, leveraging a robust set of libraries for extended functionality.

- **Backend**: Django 4.2.6, Django REST Framework, Django Crispy Forms, Django Jazzmin (for a modern admin UI).
- **Database**: The project includes a `db.sqlite3` file for development, with support for MySQL (via `mysqlclient` and `mysql-connector-python`).
- **Asynchronous Tasks**: Celery is integrated for handling background tasks, such as sending emails.
- **Other Key Libraries**: `Pillow` for image processing (likely for profile pictures), `celery` for task queues, and `pandas`/`numpy` for potential data handling.

For a complete list of dependencies, please refer to the `requirements.txt` file in the repository.

## 📁 Project Structure

The project follows a standard Django project layout with a dedicated app for each core domain:

```
Vaccination-Scheduling-Application/
├── mysite/                  # Main Django project directory
│   ├── campaign/            # App for managing vaccination campaigns
│   ├── center/              # App for managing vaccination centers
│   ├── user/                # App for user authentication and profiles
│   ├── vaccination/         # Core app for scheduling appointments
│   ├── vaccine/             # App for vaccine inventory and details
│   ├── templates/           # HTML templates
│   ├── static/              # Static files (CSS, JS, images)
│   └── manage.py            # Django's command-line utility
├── .gitignore
├── README.md
└── requirements.txt
```

This structure is visible from the repository's main page and the `mysite` directory tree.

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python (3.8 or higher recommended)
- pip
- A virtual environment tool (e.g., `venv`)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/evan-shahrukh/Vaccination-Scheduling-Application.git
    cd Vaccination-Scheduling-Application
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python mysite/manage.py migrate
    ```

5.  **Create a superuser for admin access:**
    ```bash
    python mysite/manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python mysite/manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000/`.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is currently not distributed under a specific license. Please see the repository for more details.

## 📧 Contact

Evan Shahrukh - [GitHub Profile](https://github.com/evan-shahrukh)

Project Link: [https://github.com/evan-shahrukh/Vaccination-Scheduling-Application](https://github.com/evan-shahrukh/Vaccination-Scheduling-Application)
