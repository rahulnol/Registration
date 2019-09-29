from django.urls import path
from django.conf.urls import re_path
from django.views.generic import TemplateView

from registration import views

urlpatterns = [
    path('login/',views.signin),
    path('signup/',views.signUp),

    path('test/', views.test),
    path('account/activate/', TemplateView.as_view(template_name='registration/account_activation.html')),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]