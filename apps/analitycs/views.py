from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ReportsView(TemplateView):
    template_name = 'analitycs/reports.html'
