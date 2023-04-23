from django.contrib import admin

from .models import Profile, Interest, TimelineItem

# Register your models here.
admin.site.register(Profile)


class InterestAdmin(admin.ModelAdmin):
    list_display = ['interest', 'translation', 'slug']
    search_fields = ['interest', 'translation', 'slug']

admin.site.register(Interest, InterestAdmin)
admin.site.register(TimelineItem)
