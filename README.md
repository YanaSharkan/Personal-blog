# FastAPI Personal Blog

A simple personal blog web application built with FastAPI. The blog allows you to write and publish articles, featuring a guest section for public viewing and an admin section for managing articles.

## Features

- **Guest Section**
  - Home page: View all published articles
  - Article page: View individual article content and publication date

- **Admin Section**
  - Dashboard: List, add, edit, and delete articles (admin only)
  - Add Article: Form to create new articles
  - Edit Article: Form to update existing articles
  - Delete Article: Remove articles
  - Login: Simple password-based authentication

## Tech Stack

- Python 3.7+
- FastAPI
- Jinja2 (for HTML templates)
- Pydantic

## Installation

1. Clone the repository.

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install fastapi uvicorn jinja2 pydantic
    ```

## Usage

1. Start the application:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and visit

## License

This project is for educational purposes.