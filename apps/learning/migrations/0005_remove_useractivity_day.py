# Generated by Django 4.1.7 on 2023-03-24 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_lesson_interests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useractivity',
            name='day',
        ),
    ]
