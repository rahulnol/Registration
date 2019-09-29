from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
import json

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
        newPerson.save()
        myUser = authenticate(username=email, password=password)
        login(req, myUser)
        response = {'success': True, 'error': False, 'redirect': '/dashboard/'}
        jd = json.dumps(response)
        return HttpResponse(jd, content_type='application/json')
    else:
        if (userRecord.email == email):
            response = {'success': False, 'error': True, 'errorMsg': 'Email already exists'}
            jd = json.dumps(response)
            return HttpResponse(jd, content_type='application/json')
