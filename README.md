# Sokoni Collections - E-commerce Platform

Sokoni Collections is a modern and responsive e-commerce platform built using the Flask framework. This platform is designed to provide a seamless shopping experience for users and a streamlined product management system for administrators. It supports essential features such as user authentication, product browsing, a shopping cart, order history, and a smooth checkout process.

## Features

- **User Authentication**: Secure user registration and login functionality using Flask-Login and bcrypt for password hashing.
- **Product Listings**: Dynamic product display from the database, with filtering and search capabilities.
- **Shopping Cart**: Users can add, update, or remove items from their cart.
- **Checkout Process**: Seamless checkout process integrated into the order flow, ensuring an easy user experience.
- **Order History**: Users can access their order history to view past purchases and statuses.
- **Responsive Design**: Optimized for both desktop and mobile users through Bootstrap-based design.

## Technology Stack

- **Backend**: Flask (Python Framework)
- **Database**: MySQL (Production) / SQLite (Development)
- **Frontend**: HTML, CSS, Bootstrap, Jinja2
- **ORM**: SQLAlchemy for database interactions
- **Authentication**: Flask-Login
- **Session Management**: Flask session handling

## Installation and Setup

### Prerequisites

To run the application locally, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- MySQL (For production) or SQLite (For development)
- Git

### Cloning the Repository

Clone the repository to your local machine:

```bash
git clone <repo-url>
cd sokoni-collections

file structure
ecommerce/
│
├── main.py                # Application entry point
├── requirements.txt       # List of dependencies
├── .env                   # Environment variables
├── migrations/            # Database migrations
├── sokoni/                # Main application folder
│   ├── __init__.py        # Application factory
│   ├── models.py          # Database models
│   ├── views.py           # Application views (routes)
│   ├── templates/         # HTML templates
│   ├── static/            # Static files (CSS, JS, images)
│   ├── forms.py           # WTForms for handling user input
│   ├── auth.py            # Authentication logic
│   ├── cart.py            # Cart management logic
└── tests/                 # Unit tests

