from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from utils.generator import unique_slug_generator


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Interest(models.Model):
    interest = models.CharField(max_length=100)
    translation = models.CharField(max_length=100, blank=True, null=True)

    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    users = models.ManyToManyField(get_user_model(), related_name='interests', blank=True)

    def __str__(self):
        return self.interest

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    

class TimelineItem(models.Model):

    ACTIONS_CHOICES = (
        ('0', 'daily_activity_completed'),
        ('1', 'single_lesson_completed'),
        ('2', 'custom_activity_completed'), # For repeated activities
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='timeline_items')
    action = models.CharField(max_length=100, choices=ACTIONS_CHOICES, default='0')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):

        # action = dict(self.ACTIONS_CHOICES)[self.action]

        return f'{self.user.username} - {self.action} - {self.id}'


@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_save, sender=Interest)
def save_interest(sender, instance, **kwargs):

    instance.interest = instance.interest.lower()
    instance.translation = instance.translation.lower()

    if not instance.slug:
        # create unique slug
        instance.slug = unique_slug_generator(instance, field='translation')

        