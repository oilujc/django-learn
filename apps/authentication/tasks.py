from celery import shared_task

from django.contrib.auth import get_user_model
from .services.timeline_service import TimelineService


@shared_task
def create_timeline_item(user_id, action, item_id):

    user = get_user_model().objects.get(id=user_id)

    timeline_service = TimelineService(user)
    timeline = timeline_service.create_timeline_item(action, item_id)

    if not timeline:
        return timeline_service.msg

    return True
