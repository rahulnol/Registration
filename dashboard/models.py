from django.db import models

class ImageModel(models.Model):
    url = models.URLField()
    compressed_url = models.URLField()