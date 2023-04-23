from celery import shared_task
import json

from apps.analitycs.services.process_export_service import ProcessExportService


@shared_task
def export_data_task(report_id: int):
    process = ProcessExportService().process(report_id)

    return True