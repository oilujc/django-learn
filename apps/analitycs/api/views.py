from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from apps.analitycs.api.serializers import ReportSerializer


from apps.analitycs.models import Report

from apps.analitycs.services.export_data_service import ExportDataService


class ReportGeneratorView(ViewSet):
    """
    This class is used to generate a report.
    """
    lookup_field = 'slug'

    def create(self, request):
        """
        This method is used to generate a report.
        """

        if not 'report_type' in request.data:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        report = ExportDataService().export_data(request.data['report_type'])
        serializer = ReportSerializer(report, context={'request': request})


        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def list(self, request):
        """
        This method is used to get a report.
        """

        qs = Report.objects.all()
        serializer = ReportSerializer(
            qs,
            many = True,
            context={'request': request}
        )


        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def retrieve(self, request, slug=None):
        """
        This method is used to get a report.
        """ 

        if not slug:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            qs = Report.objects.get(slug=slug)
        except Report.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReportSerializer(
            qs,
            context={'request': request}
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )