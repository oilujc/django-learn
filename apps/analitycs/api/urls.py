from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ReportGeneratorView

router = DefaultRouter()
router.register(r'reports', ReportGeneratorView, basename='reports')

app_name = 'analitycs_api'
urlpatterns = [
] + router.urls