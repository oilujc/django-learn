from rest_framework import serializers
from apps.analitycs.models import Report



class ReportSerializer(serializers.ModelSerializer):

    file = serializers.SerializerMethodField()


    class Meta:
        model = Report
        fields = (
            'id',
            'name',
            'slug',
            'file',
            'filters',
            'task_id',
            'task_status',
            'report_type',
            'created_at',
            'updated_at'
        )

    def get_file(self, obj):

        if not obj.file:
            return None

        # get full url
        return self.context['request'].build_absolute_uri(obj.file.url)