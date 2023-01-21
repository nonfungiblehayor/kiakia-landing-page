from django.db import models
from datetime import datetime

# Create your models here.


class Mail(models.Model):
    email = models.EmailField(max_length=300)
    date = models.DateTimeField(default=datetime.now, blank=True)
