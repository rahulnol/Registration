from django.shortcuts import render
from django.views import View

class DashboardView(View):

    def get(self, req, *args, **kwargs):
        return render(req, 'dashboard.html', context={})
