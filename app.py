from flask import Flask, request, render_template, Response
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde el archivo .env

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    emails = request.form.get('email').split(',')  # Separar correos electrónicos por comas
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Verificar si todos los datos están presentes
    if not emails or not subject or not message:
        return Response('Faltan datos del formulario', status=400, content_type='text/plain; charset=utf-8')

    # Limpiar y verificar las direcciones de correo electrónico
    emails = [email.strip() for email in emails if email.strip()]

    # Imprimir el contenido del mensaje para depuración
    print(f"Received emails: {emails}")
    print(f"Subject: {subject}")
    print(f"Message: {message}")

    # Verificar tipo y contenido de `message`
    if not isinstance(message, str):
        return Response('El mensaje no es una cadena de texto válida', status=400, content_type='text/plain; charset=utf-8')

    # Enviar el correo electrónico a todos los destinatarios
    send_mail(emails, subject, message)

    return Response('Email sent to all recipients!', content_type='text/plain; charset=utf-8')

def send_mail(to_emails, subject, message):
    from_email = os.getenv('EMAIL_USER')
    from_password = os.getenv('EMAIL_PASS')

    # Verificar si las credenciales están configuradas correctamente
    if not from_email or not from_password:
        print("Error: Las credenciales de correo no están configuradas correctamente.")
        return

    # Verificar si el mensaje es None y establecer un valor predeterminado
    if message is None:
        message = ""

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)  # Añadir todos los destinatarios al campo 'To'
    msg['Subject'] = subject

    # Asegúrate de que el cuerpo del mensaje use UTF-8
    part = MIMEText(message, 'plain', 'utf-8')
    msg.attach(part)

    try:
        # Conectar al servidor SMTP de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Inicia la conexión segura
        server.login(from_email, from_password)  # Autenticación

        # Enviar el correo a todos los destinatarios
        text = msg.as_string()  # Convierte el mensaje a una cadena
        server.sendmail(from_email, to_emails, text)  # Envía el correo

        server.quit()  # Cierra la conexión
        print("Email sent successfully to all recipients")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)









