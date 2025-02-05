# Generated by Django 5.1.5 on 2025-02-04 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titlemodel',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='titlemodel',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='titlemodel',
            name='page_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='titlemodel',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
