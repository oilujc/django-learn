from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.learning.services.user_activity_service import UserActivityService

# Create your views here.
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

class TimelineView(LoginRequiredMixin, TemplateView):
    template_name = 'user/timeline.html'