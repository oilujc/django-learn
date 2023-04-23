from django import template

from apps.learning.services.activity_progress_service import ActivityProgresService



register = template.Library()

@register.filter(name='lesson_type')
def lesson_type_handler(lesson):
    return dict(lesson.LESSON_TYPE_CHOICES)[lesson.lesson_type]

@register.inclusion_tag('user/lesson_check.html')
def is_lesson_completed(activity, lesson):

    activity_progress_service = ActivityProgresService(activity)

    return {
        'is_completed': activity_progress_service.check_if_progress_exists(lesson)
    }
    