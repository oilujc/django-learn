import os
from django.db import models

from django.contrib.postgres.fields import ArrayField
from utils.generator import random_string_generator

from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
def upload_location(instance, filename):
    return 'reports/%s' % (filename)


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.csv']
    if not ext.lower() in valid_extensions:
        raise Exception(u'Unsupported file extension.')

class Report(models.Model):


    REPORT_TYPES_CHOICES = (
        ('activity', 'Activity'),
        ('user', 'User'),
        ('lesson', 'Lesson'),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    file = models.FileField(upload_to=upload_location, null=True, blank=True, 
                            validators=[validate_file_extension]) # only csv files
    
    filters = ArrayField(models.CharField(max_length=100), null=True, blank=True)

    task_id = models.CharField(max_length=255, null=True, blank=True)
    task_status = models.CharField(max_length=255, null=True, blank=True)
    
    report_type = models.CharField(max_length=255, choices=REPORT_TYPES_CHOICES, default='activity')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


@receiver(pre_save, sender=Report)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = random_string_generator(size=16)