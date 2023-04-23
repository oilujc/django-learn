from typing import Any
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

from apps.learning.services.activity_progress_service import ActivityProgresService
from apps.learning.services.user_activity_service import UserActivityService




# Create your views here.

class InterestsView(LoginRequiredMixin, TemplateView):
    template_name = 'learning/interests.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            if request.user.interests.count() > 0:
                return redirect('learning:learning')

        return super().dispatch(request, *args, **kwargs)


class LearningView(LoginRequiredMixin, TemplateView):
    template_name = 'learning/learning.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        if request.user.is_authenticated:
            if request.user.interests.count() == 0:
                return redirect('learning:interests')
            
            self.user_activity_service = UserActivityService(request.user)

            activity = request.GET.get('a', None)

            if activity:
                self.user_activity_service.set_activity(activity)


            self.activity_progress = ActivityProgresService(self.user_activity_service.activity)

        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)

        
        context['activity'] = self.user_activity_service.activity
        context['next_lesson'] = None

        lessons = self.activity_progress.get_next_lesson(num=2) 

        if not lessons:
            context['lesson'] = None
        else:
            context['lesson'] = lessons[0]

            if len(lessons) > 1:
                context['next_lesson'] = lessons[1]

        return context
    
