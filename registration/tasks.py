import string

from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string

from celery import shared_task
from django.utils.http import urlsafe_base64_encode
from jwt.utils import force_bytes

from django.conf import settings
from registration.tokens import account_activation_token

@shared_task
def send_activation_email(req, user):
    current_site = get_current_site(req)
    message = render_to_string('registration/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(str(user.pk))).decode("utf-8"),
        'token': account_activation_token.make_token(user),
    })
    send_mail('Please confirm your email address', message, settings.EMAIL_HOST_USER, [user.email])

    return 'Activation link email sent to user successfully'

@shared_task
def add(x, y):
    return x + y