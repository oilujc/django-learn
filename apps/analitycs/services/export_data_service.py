from typing import TypeVar

from datetime import datetime

from apps.analitycs.models import Report
from apps.analitycs.services.activity_export_service import ActivityExportService
from apps.analitycs.tasks import export_data_task

R = TypeVar('R', bound=Report)

class ExportDataService:

    SERVICES = {
        # 'User': UserExportService,
        'activity': ActivityExportService,
    }

    @classmethod
    def export_data(self, report_type: str) -> R:

        # get date
        date = datetime.now().strftime("%Y%m%d-%H%M%S")

        # validate data
        if not report_type in self.SERVICES:
            raise Exception('Invalid report type')
        
        # create report
        report = Report.objects.create(
            name=f'{report_type}-{date}',
            report_type=report_type,
        )
            
        # call task
        export_data_task.delay(report.id)

        return report

