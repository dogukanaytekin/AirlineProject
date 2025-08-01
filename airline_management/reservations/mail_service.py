from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os 

def send_reservation_confirmation_email(email):
    subject = "Reservation Confirmation"
    message = "Your reservation has been successfully created. We wish you a pleasant journey!"
    from_email = "dogukanaytekin35@gmail.com"
    recipient_list = [email]

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)

    email_message = EmailMessage(subject,message,from_email,recipient_list)
    try:
        email_message.attach_file(BASE_DIR+"/images.png")
    except:
        pass
    email_message.send()
