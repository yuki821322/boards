from django.db import models
from datetime import date

# Create your models here.


# class TitleModel(models.Model):
#     title = models.CharField(max_length=10)


class TitleModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PostModel(models.Model):
    title = models.ForeignKey(TitleModel, on_delete=models.CASCADE)  # タイトルと紐づけ
    date = models.DateField(default=date.today)
    page_number = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title.title} - {self.date}"
