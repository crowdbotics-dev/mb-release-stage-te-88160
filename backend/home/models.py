from django.conf import settings
from django.db import models
class Main(models.Model):
    'Generated Model'
    tappi = models.EmailField(max_length=254,)
