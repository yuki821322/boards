from django.db import models

# Create your models here.


class TitleModel(models.Model):
    title = models.CharField(max_length=10)
