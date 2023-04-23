from django.urls import path

from . import views


app_name = 'analitycs'
urlpatterns = [
    path('reports/', views.ReportsView.as_view(), name='reports'),
]