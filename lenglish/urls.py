"""lenglish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),


    path('auth/', include('apps.authentication.urls', namespace='authentication')),
    path('account/', include('apps.authentication.user_urls', namespace='user')),
    path('learning/', include('apps.learning.urls', namespace='learning')),
    path('feed/', include('apps.explore.urls', namespace='explore')),
    path('analitycs/', include('apps.analitycs.urls', namespace='analitycs')),

    path('api/user/', include('apps.authentication.api.urls', namespace='user_api')),
    path('api/learning/', include('apps.learning.api.urls', namespace='learning_api')),
    path('api/analitycs/', include('apps.analitycs.api.urls', namespace='analitycs_api')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
