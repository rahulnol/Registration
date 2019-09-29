import json

from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from jwt.utils import force_bytes
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from registration.tokens import account_activation_token

def signin(req):
    email = req.POST.get('email', False)
    password = req.POST.get('password', False)

    try:
        userRecord = User.objects.get(Q(email=email))
    except User.DoesNotExist:
        resp = {'success': False, 'error': True, 'errorMsg': 'Invalid login credentials'}
        jd = json.dumps(resp)
        return HttpResponse(jd, content_type='application/json')
    else:
        if not userRecord.is_active:
            resp = {'success': False, 'error': True, 'errorMsg': 'Please verify your account first.'}
            jd = json.dumps(resp)
            return HttpResponse(jd, content_type='application/json')

        user = authenticate(username=userRecord.username, password=password)
        if (user is None):
            resp = {'success': False, 'error': True, 'errorMsg': 'Invalid login credentials'}
            jd = json.dumps(resp)
            return HttpResponse(jd, content_type='application/json')
        else:
            login(req, user)
            resp = {'success': True, 'error': False, 'redirect': '/dashboard/'}
            jd = json.dumps(resp)
            return HttpResponse(jd, content_type='application/json')


def signUp(req):
    email = req.POST.get('email', False)
    password = req.POST.get('password', False)
    try:
        userRecord = User.objects.get(email=email)
    except User.DoesNotExist:
        newPerson = User(email=email, username=email)
        newPerson.set_password(password)
        newPerson.is_active = False
        newPerson.save()
        current_site = get_current_site(req)
        message = render_to_string('registration/account_activation_email.html', {
            'user': newPerson,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(str(newPerson.pk))).decode("utf-8"),
            'token': account_activation_token.make_token(newPerson),
        })
        send_mail('Please confirm your email address', message, settings.EMAIL_HOST_USER, [newPerson.email])

        response = {'success': True, 'error': False, 'redirect': '/account/activate/'}
        jd = json.dumps(response)
        return HttpResponse(jd, content_type='application/json')
    else:
        if (userRecord.email == email):
            response = {'success': False, 'error': True, 'errorMsg': 'Email already exists'}
            jd = json.dumps(response)
            return HttpResponse(jd, content_type='application/json')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/dashboard/')
    return redirect('/')
