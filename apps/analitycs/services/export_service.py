import os
from typing import TypeVar
from apps.analitycs.models import Report

from django.conf import settings


R = TypeVar('R', bound=Report)

class ExportService:

    @classmethod
    def get_media_url(cls, filename: str) -> str:
        filepath = os.path.join(settings.MEDIA_ROOT, 'reports', filename)

        print(filepath)

        return filepath

    @staticmethod
    def export(report: R) -> R:
        pass