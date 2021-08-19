from django.core.mail import send_mail
from django.conf import settings

from fees.helpers.email_helper.html_rendering import invite_template, base_template


def send_invite_email(recipients, first_name, one_time_password):
    subject = "You have been invited!"
    invite_content = invite_template.format(first_name=first_name, password=one_time_password)
    base = base_template

    content = base.format(content=invite_content)
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, "", email_from, recipients, html_message=content)
