# Generated by Django 4.1.7 on 2023-03-29 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_timelineitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timelineitem',
            name='item',
        ),
    ]
