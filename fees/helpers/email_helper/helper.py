from django.core.mail import send_mail
from django.conf import settings

from fees.fees.models import Fee
from fees.helpers.email_helper.html_rendering import invite_template, base_template
from fees.users.models import User


def send_invite_email(recipients, first_name, one_time_password):
    subject = "You have been invited!"
    invite_content = invite_template.format(first_name=first_name, password=one_time_password)
    base = base_template

    content = base.format(content=invite_content)
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, "", email_from, recipients, html_message=content)


def send_fee_email(recipients_ids, fees_ids):
    subject = "You have been invited!"
    recipients = User.objects.filter(id__in=recipients_ids)
    fees = Fee.objects.filter(id__in=fees_ids)
    fee_content = invite_template.format(fees=[f"<li>{fee.name}({fee.price})</li>\n"for fee in fees])
    base = base_template

    content = base.format(content=fee_content)
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, "", email_from, [recipient.email for recipient in recipients], html_message=content)
