# Generated by Django 4.1.7 on 2023-03-26 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0015_lesson_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityprogress',
            name='next_lesson_type',
            field=models.CharField(blank=True, choices=[('0', 'Conversation'), ('1', 'Grammar'), ('2', 'Vocabulary'), ('3', 'Word Reinforcement'), ('4', 'Quiz')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('0', 'Conversation'), ('1', 'Grammar'), ('2', 'Vocabulary'), ('3', 'Word Reinforcement'), ('4', 'Quiz')], default='0', max_length=1),
        ),
    ]
