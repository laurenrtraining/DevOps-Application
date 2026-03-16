import hashlib
from flask_mail import Mail, Message
import os

salt = "5gz"


def hash_password(password):
    password_salt = password + salt
    return hashlib.sha256(password_salt.encode()).hexdigest()


mail = Mail()


def init_mail(app):
    app.config["MAIL_SERVER"] = "sandbox.smtp.mailtrap.io"
    app.config["MAIL_PORT"] = 2525
    app.config["MAIL_USERNAME"] = "ab741a370ac58d"
    app.config["MAIL_PASSWORD"] = "c3ae731c8b6956"
    app.config["MAIL_USE_SSL"] = False
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_DEFAULT_SENDER"] = "SocialSocieties <noreply@socialsocieties.com>"

    mail.init_app(app)


def send_email(to_email, code):
    if mail is None:
        raise RuntimeError(
            "Mail not working. Contact Administrator. Initialise App first"
        )

    message = Message(
        subject="Your MFA Verification Code",
        recipients=[to_email],
        body=f"Your code is: {code} \n It expires in 5 minutes",
    )
    mail.send(message)
