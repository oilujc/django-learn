from typing import TypeVar
import pandas as pd

from datetime import datetime
from apps.analitycs.services.export_service import ExportService

from apps.learning.models import UserActivity
from apps.analitycs.models import Report

from django.core.files.base import ContentFile


R = TypeVar('R', bound=Report)

class ActivityExportService(ExportService):

    @classmethod
    def export(cls, report: R) -> R:

        # get timestamp
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")

        # Export activity to a file
        data = UserActivity.objects.all()
        df = pd.DataFrame(data)

        # Create file and add in contentfile
        filepath = ContentFile(df.to_csv(index=False).encode('utf-8'))

        report.file.save(f'{timestamp}.csv', filepath)

        # add file to report
        report.save()

        return report