from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ExploreView(TemplateView):
    template_name = 'explore/explore.html'
