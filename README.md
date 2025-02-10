# AI Note Taker

AI Note Taker is an intelligent meeting assistant that automates the process of recording, transcribing, summarizing, and emailing meeting notes. Built with Django, Selenium, Speech Recognition, PostgreSQL, and TensorFlow, this project streamlines note-taking during Google Meet sessions.

## Features

- **User Authentication with Email Verification**
- **Google Meet Integration using Selenium**
- **Automated Meeting Recording**
- **Real-time Speech Recognition & Transcription**
- **AI-Powered Summary using TensorFlow**
- **Automated Email Delivery of Meeting Notes**

## Tech Stack

- **Backend:** Django (Python)
- **Automation:** Selenium
- **Speech Processing:** SpeechRecognition Library
- **Database:** PostgreSQL
- **AI Summary:** TensorFlow
- **Email Service:** Django Email Backend

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Chrome & ChromeDriver (for Selenium)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI_Note_Taker.git
   cd AI_Note_Taker
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure PostgreSQL:
   - Create a PostgreSQL database and update `settings.py` with your credentials.

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the Django server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Register/Login:**
   - Users sign up using their email and receive a verification link.

2. **Provide Google Meet Code:**
   - Enter the Google Meet code into the web interface.

3. **Automated Meeting Attendance:**
   - Selenium launches the browser, joins the Google Meet session, and starts recording.

4. **Transcription & Summarization:**
   - Speech is transcribed in real time.
   - TensorFlow processes and summarizes the transcript.

5. **Email Summary:**
   - The summarized notes are emailed to the user automatically.

## Environment Variables

Create a `.env` file in the project root and define:
```
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
POSTGRES_DB=your-db-name
POSTGRES_USER=your-db-user
POSTGRES_PASSWORD=your-db-password
```

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and test them.
4. Submit a pull request.


