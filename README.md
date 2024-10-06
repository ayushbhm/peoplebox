# PeopleBox - Job Recommendation System
FLASK backend to recommend jobs based on input
## Table of Contents


- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Overview](#api-overview)
- [Assumptions](#assumptions)
- [API Endpoints](#api-endpoints)



## Technologies

This project is built using the following technologies:

- **Python**: The programming language used for backend development.
- **Flask**: A lightweight web framework for building the API.
- **Flask-SQLAlchemy**: An ORM for managing database interactions.
- **SQLite**: A simple database for storing user profiles and job postings.

## Getting Started

To get a local copy of this project up and running, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ayushbhm/peoplebox.git
   cd peoplebox
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the API**: Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

You can interact with the API using tools like Postman or cURL. Here’s how to make a request to get job recommendations:

### Example Request

```json
{
  "name": "Jane Doe",
  "skills": ["Python", "Django", "REST APIs"],
  "preferences": {
    "desired_roles": ["Backend Developer", "Software Engineer"],
    "locations": ["Remote", "New York"],
    "job_type": "Full-Time"
  }
}
```

## API Overview

The job recommendation API is designed to match job seekers with suitable job postings based on their skills, experience, and preferences. It takes user input in the form of a JSON object and processes this data to generate a list of job recommendations.

### Key Components of the API

1. **Input Data**: The API expects a JSON object containing the user's name, skills, and preferences (desired roles, locations, and job type).

2. **Database Models**: The API interacts with several database models, including UserProfile, JobPosting, Skill, and Location.

3. **Recommendation Logic**: The API uses a scoring system to evaluate job postings based on the user's input, considering factors like desired roles, job type, location, and matching skills.

4. **Output Data**: The API returns a JSON array of job recommendations, each containing job details and a calculated score.

## Assumptions

1. **Data Integrity**: The API assumes that the data in the database (job postings, skills, and locations) is accurate and up-to-date.

2. **User Input**: The API assumes that the user will provide valid input in the expected format. If the input is missing required fields, the API will return a 400 Bad Request error.



## API Endpoints

### POST /recommend_jobs

- **Request Body**: JSON object containing user profile data.
- **Response**: A list of job recommendations based on the provided profile.

### Example Response

```json
[
  {
    "job_title": "Backend Developer",
    "company": "Tech Solutions Inc.",
    "location": "Remote",
    "job_type": "Full-Time",
    "required_skills": ["Python", "Django"],
    "experience_level": "Intermediate",
    "score": 5
  }
]
```
