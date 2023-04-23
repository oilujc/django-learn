# Generated by Django 4.1.7 on 2023-03-27 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0023_lessonlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivityrating',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='activity_ratings', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]