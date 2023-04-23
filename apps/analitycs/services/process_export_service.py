from typing import TypeVar

from datetime import datetime
from apps.analitycs.models import Report
from apps.analitycs.services.activity_export_service import ActivityExportService


R = TypeVar('R', bound=Report)



class ProcessExportService:
    SERVICES = {
        # 'User': UserExportService,
        'activity': ActivityExportService,
    }

    @classmethod
    def process(cls, report_id: int) -> R:

        report = Report.objects.get(id=report_id)
        return cls.SERVICES[report.report_type].export(report)



        
