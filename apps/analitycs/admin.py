from django.contrib import admin
from .models import Report
# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'report_type', 'created_at', 'updated_at')
    list_filter = ('report_type', 'created_at', 'updated_at')
    search_fields = ('name', 'report_type', 'created_at', 'updated_at')


admin.site.register(Report , ReportAdmin)