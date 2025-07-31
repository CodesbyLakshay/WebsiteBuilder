# WebsiteBuilder

### Build Stunning Websites Faster, Smarter, and Securely

Built with the tools and technologies:
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

---

### Table of Contents
1. [Overview](#overview)
2. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
3. [Usage](#usage)
4. [API Endpoints](#api-endpoints)
5. [Testing](#testing)

---

## Overview

WebsiteBuilder is a powerful backend solution designed to simplify the creation, management, and security of web applications. It provides a complete toolkit for developers, featuring robust authentication, granular role-based permissions, AI-powered content generation, and dynamic website previews.

### Why WebsiteBuilder?

This project helps developers streamline app security, configuration, and website content management. The core features include:

🛡️ **Secure Authentication**: Implements JWT-based authentication for secure user sessions and API access.
🚦 **Role-Based Access Control**: Utilizes middleware to enforce permissions for `Admin`, `Editor`, and `Viewer` roles, safeguarding sensitive endpoints.
🤖 **AI Content Generation**: Features an endpoint ready to integrate with AI models (like OpenAI or Hugging Face) to generate website content based on user prompts.
🌐 **Dynamic Website Preview**: Dynamically renders website content using Flask and Jinja2, providing a live preview before deployment.
📁 **Full CRUD Operations**: Manages website and user data efficiently with built-in MongoDB interactions.
⚙️ **Centralized Configuration**: Simplifies environment-specific settings for seamless deployment using a `.env` file.
🚀 **Easy App Initialization**: Provides a streamlined startup script (`run.py`) for local development and testing.

---

## Getting Started

### Prerequisites

This project requires the following to be installed on your system:
* **Python 3.8+**
* **pip** (Python package installer)
* **MongoDB** running locally or a connection URI.

### Installation

Build WebsiteBuilder from the source and install dependencies:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/CodesbyLakshay/WebsiteBuilder](https://github.com/CodesbyLakshay/WebsiteBuilder)
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd WebsiteBuilder
    ```

3.  **Create and activate a virtual environment:**
    * On macOS/Linux:
        ```sh
        python3 -m venv .venv
        source .venv/bin/activate
        ```
    * On Windows:
        ```sh
        python -m venv .venv
        .venv\Scripts\activate
        ```

4.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5.  **Configure Environment Variables:**
    * Create a file named `.env` in the root directory.
    * Add the following variables. You can generate a new `JWT_SECRET_KEY` using the `generate_jwt_key.py` script.
        ```env
        MONGO_URI="mongodb://localhost:27017/website_builder"
        JWT_SECRET_KEY="your_super_secret_jwt_key_here"
        HUGGINGFACE_API_KEY="your_huggingface_api_key_optional"
        ```

---

## Usage

Run the project with the following commands after activating your virtual environment:

1.  **Activate the virtual environment** (if not already active):
    * On macOS/Linux:
        ```sh
        source .venv/bin/activate
        ```
    * On Windows:
        ```sh
        .venv\Scripts\activate
        ```

2.  **Run the Flask application:**
    ```sh
    python run.py
    ```
    The application will start on `http://127.0.0.1:5000`.

---

## API Endpoints

The application exposes several API endpoints for authentication, website management, and admin controls. You can find a complete list of cURL commands to interact with these endpoints in Postman or a similar API client.

Key endpoints include:
* `/signup`, `/login`
* `/websites`, `/websites/<id>`
* `/preview/<id>`
* `/admin/users`, `/admin/users/<id>`, `/admin/roles`

---

## Testing

This project is set up for testing with `pytest`. To run the test suite, use the following command after activating your virtual environment:

```sh
pytest
