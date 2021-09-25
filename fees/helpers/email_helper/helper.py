from time import sleep

from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from fees.fees.models import Fee
from fees.helpers.email_helper.html_rendering import invite_template, base_template, fee_email
from fees.teams.models import Team
from fees.users.models import User


@shared_task(name="send_invite_email")
def send_invite_email(recipients, first_name, one_time_password):
    sleep(10)
    subject = "You have been invited!"
    invite_content = invite_template.format(first_name=first_name, password=one_time_password)
    base = base_template

    content = base.format(content=invite_content)
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, "", email_from, recipients, html_message=content)


@shared_task(name="send_fee_email")
def send_fee_email(recipients_ids, fees_ids, team_id):
    subject = "New fee(s) have been added!"
    recipients = User.objects.filter(id__in=recipients_ids)
    fees = Fee.objects.filter(id__in=fees_ids)
    team = Team.objects.get(id=team_id)
    fee_content = fee_email.format(
        fees="\n".join([f"<li>{fee.name} (<small>{team.currency}</small> <b>{fee.price}</b>)</li>"for fee in fees])
    )
    base = base_template

    content = base.format(content=fee_content)
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, "", email_from, [recipient.email for recipient in recipients], html_message=content)
