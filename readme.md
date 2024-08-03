User Management System

Overview

A comprehensive system for managing user accounts, profiles, and roles, including professional status upgrades, user search, and filtering.

Table of Contents

Installation
Usage
API Documentation
Contributing
Testing
License
Authors and Acknowledgments
Installation

Clone the repository:
git clone https://github.com/tishamadhok/user_management.git

Navigate to the project directory:
cd user_management

Set up the environment:
Create a .env file and configure it with your environment variables (e.g., MailTrap settings).

Build and run the project:
docker compose up --build

Usage

Access the API documentation at http://localhost/docs to explore the endpoints and test the functionalities.

API Documentation

Profile Update
Endpoint: /user/profile/update
Method: PUT
Description: Update user profile details like name, bio, and more.
Professional Status Upgrade
Endpoint: /admin/user/professional-status
Method: POST
Description: Upgrade a user's professional status (Admin only).
User Search and Filtering
Endpoint: /users
Method: GET
Description: Search and filter users by username, email, role, and other criteria.
Query Parameters:
username (optional): Search by username.
email (optional): Search by email.
role (optional): Filter by user role.
created_before (optional): Filter users created before a specific date.
created_after (optional): Filter users created after a specific date.
is_active (optional): Filter by active status.
Contributing

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes and commit (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a Pull Request.
Testing

Run tests using:
docker compose exec fastapi pytest

License

This project is licensed under the MIT License. See the LICENSE file for details.

Authors and Acknowledgments

Tisha Madhok