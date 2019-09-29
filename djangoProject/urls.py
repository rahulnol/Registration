from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('registration.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', TemplateView.as_view(template_name='index.html'))

]
