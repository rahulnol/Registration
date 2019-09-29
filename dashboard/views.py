import contextlib, json
from urllib.parse import urlencode
from urllib.request import urlopen
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import ImageModel


class DashboardView(View):

    def get(self, req, *args, **kwargs):
        return render(req, 'dashboard.html', context={})

    def post(self, req, *args, **kwargs):
        data = req.POST.get('data', []);
        data = json.loads(data)
        for url in data:
            try:
                request_url = ('http://tinyurl.com/api-create.php?' +
                               urlencode({'url': url}))
                with contextlib.closing(urlopen(request_url)) as response:
                    compress_url = response.read().decode('utf-8')
            except:
                compress_url = url

            ImageModel.objects.create(
                url=url, compressed_url=compress_url
            )
        return HttpResponse({'success': True})
