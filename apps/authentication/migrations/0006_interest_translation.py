# Generated by Django 4.1.7 on 2023-03-25 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_interest_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='translation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
