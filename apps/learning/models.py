from django.db import models
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django_quill.fields import QuillField

from utils.generator import unique_slug_generator, random_string_generator

# Create your models here.

def lesson_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'lesson_{0}/{1}'.format(instance.lesson.id, filename)

class Word(models.Model):

    word = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    definition = models.TextField()

    pronunciation = models.CharField(max_length=100, blank=True, null=True)
    translation = models.CharField(max_length=100, blank=True, null=True)

    image = models.ImageField(upload_to=lesson_directory_path, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.word

class WordExample(models.Model):

    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='examples')
    example = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.example

class Lesson(models.Model):

    LESSON_TYPE_CHOICES = (
        ('0', 'Conversation'), # Create a conversation, and then have the user chech whats words doesnt he know
        ('1', 'Grammar'),
        ('2', 'Word Reinforcement'), # 
        ('3', 'Quiz'),
        ('4', 'Story'),
    )

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    
    content = QuillField()
    short_description = models.CharField(max_length=255)

    lesson_type = models.CharField(max_length=1, choices=LESSON_TYPE_CHOICES, default='0')

    image = models.ImageField(upload_to=lesson_directory_path, blank=True, null=True)
    level = models.IntegerField(default=0) # 0 - 5 (0 - beginner, 5 - advanced)

    interests = models.ManyToManyField('authentication.Interest', related_name='lessons', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Question(models.Model):
        
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    level = models.IntegerField(default=1)
    lessons = models.ManyToManyField(Lesson, related_name='questions', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    

class UserAnswer(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    answer = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.question.question}'

class LessonRating(models.Model):
    
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='ratings')

    rating = models.IntegerField(default=0)
    is_valid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.lesson.title}'
    
class LessonLike(models.Model):

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_likes')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_likes')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.lesson.title} - {self.user.username}'

class UserActivity(models.Model):
    
    '''
        This model will be created when the user "starts a lesson"
        - max lessons per day is 5
        - lessons are selected based on the user's interests
        - lessons level is selected based on the user's score
        - lessons are selected based on the user's progress
    '''

    USER_ACTIVITY_TYPE_CHOICES = (
        ('0', 'Daily'),
        ('1', 'User Created'),
        ('2', 'User Joined'),
        ('3', 'User Repeated'),
    )

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    user_activity_type = models.CharField(max_length=1, choices=USER_ACTIVITY_TYPE_CHOICES, default='0')

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    lessons = models.ManyToManyField(Lesson, related_name='user_activity', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.title}'
    
class UserActivityLike(models.Model):

    activity = models.ForeignKey(UserActivity, on_delete=models.CASCADE, related_name='followers')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='following')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.activity.title} - {self.user.username}'


class UserActivityRating(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='activity_ratings')
    activity = models.ForeignKey(UserActivity, on_delete=models.CASCADE, related_name='ratings')

    rating = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.activity.title}'



class ActivityProgress(models.Model):


    activity = models.ForeignKey(UserActivity, on_delete=models.CASCADE, related_name='progress')
    lesson = models.ForeignKey('learning.Lesson', on_delete=models.CASCADE)    

    words = models.ManyToManyField('learning.Word', related_name='user_progress', blank=True)
    next_lesson = models.ForeignKey('learning.Lesson', on_delete=models.CASCADE, related_name='next_lesson', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.activity.user.username} - {self.lesson.title}'
    
class ActivityTimeline(models.Model):
    timeline = models.ForeignKey('authentication.TimelineItem', on_delete=models.CASCADE, related_name='timeline')
    activity = models.ForeignKey(UserActivity, on_delete=models.CASCADE, related_name='activity')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LessonTimeline(models.Model):
    timeline = models.ForeignKey('authentication.TimelineItem', on_delete=models.CASCADE, related_name='lesson_timeline')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

@receiver(pre_save, sender=Lesson)
def slugify_lesson(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


@receiver(pre_save, sender=Word)
def slugify_word(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, field='word')

@receiver(pre_save, sender=UserActivity)
def slugify_activity(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = random_string_generator(size=16)