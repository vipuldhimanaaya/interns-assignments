import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach body
    message.attach(MIMEText(body, 'plain'))

    # Attach image
    if attachment_path:
        attach_image(message, attachment_path)

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())

def attach_image(message, attachment_path):
    with open(attachment_path, 'rb') as attachment:
        # Determine the file type
        file_type = attachment_path.split('.')[-1].lower()
        if file_type in ['png', 'jpg', 'jpeg']:
            image = MIMEImage(attachment.read(), name='image.' + file_type)
            message.attach(image)
        else:
            raise ValueError("Only images of type PNG, JPG, JPEG are allowed.")

if __name__ == "__main__":
    # Replace these with your personal email and password
    sender_email = "vipuldhiman201801@gmail.com"
    sender_password = "app password"
    # cannot share app password

    receiver_email = "hr@ignitershub.com"
    subject = "Challenge 3 Completed"

    # Add your details to the email body
    body = """Your Name: Vipul
Semester: pass out
Branch: Computer Science
Roll Number: 2002004511
"""

    # Specify the path to your image file (PNG, JPG, JPEG)
    attachment_path = "sendMailImg.jpg"

    try:
        send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
