# BoilerMenu

**Your Meal, Your Way!**

BoilerMenu is a web application built around Purdue dining menus. It allows students to browse dining information and personalize their experience based on their food preferences.

## Features

* Browse Purdue dining menus
* User registration and authentication
* Personalized food preferences
* Item-level preferences
* User dashboard
* Purdue dining menu data
* Responsive web interface

## Overview

Purdue dining menus contain a large amount of information that can be difficult to navigate when looking for specific foods or preferences.

BoilerMenu organizes this information into a user-friendly application while allowing users to save preferences and personalize the information they see.

## Technologies

* **Backend:** Python, Django 5.1
* **Frontend:** HTML, CSS, Django Templates
* **Database:** Django ORM
* **Authentication:** Django Authentication Framework

## Project Structure

```text
BoilerMenu/
├── Menus/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   └── static/
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── manage.py
```

## Running Locally

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Install Django and the required dependencies:

```bash
pip install django
```

Apply the database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then open the local development server in your browser.

## Project Goal

BoilerMenu was designed to make Purdue dining information easier to navigate by combining dining data with personalized user preferences in a single application.
