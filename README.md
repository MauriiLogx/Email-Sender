# Email Sender

## Description

This is an "email sender" project developed with Flask. It allows you to send emails through a simple web interface. The project uses Flask for the backend and SMTP for sending emails.

## Features

- Send emails via a web form.
- Support for SMTP server configuration.
- Simple and user-friendly web interface.

## Technologies Used

- **Flask**: A micro-framework for Python that makes web development easier.
- **SMTP**: Simple Mail Transfer Protocol for sending emails.
- **HTML**: For creating web forms.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/email-sender.git

2. Navigate to the project directory:
   ```bash
   cd email-sender
   
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt

5. Configure the config.py file with your SMTP server credentials:
   ```python
   MAIL_SERVER = 'smtp.example.com'
   MAIL_PORT = 587
   MAIL_USERNAME = 'youremail@example.com'
   MAIL_PASSWORD = 'yourpassword'
   MAIL_USE_TLS = True

6. Run the application:
   ```python
   python app.py

7. Access the web interface at http://127.0.0.1:5000.

# Usage
1. Open the application in your web browser.
2. Fill out the form with the email details:
   - Recipient
   - Subject
   - Body of the message
3. Click "Send" to send the email.

# Contributing
Contributions are welcome. If you have suggestions or improvements, please open an issue or a pull request.

# License 
This project is licensed under the MIT License. See the LICENSE file for more details.

# Contact
For any questions or comments, you can reach me at maurii_181@hotmail.com.
