from django.contrib import admin
from .models import (Word,
    WordExample,
    Lesson,
    UserActivity,
    ActivityProgress,
    LessonRating,
    UserActivityRating,
    UserActivityLike,
    LessonLike,
    ActivityTimeline,
    LessonTimeline
)


# Register your models here.
admin.site.register(Word)
admin.site.register(WordExample)


class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'level', 'lesson_type', 'parent', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'level' )
    ordering = ('-created_at',)
    actions = [
        'change_to_quiz',
        'change_to_word_reinforcement',
        'change_to_conversation',
        'change_to_grammar',
        'change_to_level_5',
        'change_to_level_4',
        'change_to_level_3',
        'change_to_level_2',
        'change_to_level_1'
    ]

    def change_to_grammar(self, request, queryset):
        queryset.update(lesson_type=1)

    def change_to_quiz(self, request, queryset):
        queryset.update(lesson_type=4)

    def change_to_conversation(self, request, queryset):
        queryset.update(lesson_type=0)

    def change_to_word_reinforcement(self, request, queryset):
        queryset.update(lesson_type=3)
    
    def change_to_level_5(self, request, queryset):
        queryset.update(level=5)

    def change_to_level_4(self, request, queryset):
        queryset.update(level=4)

    def change_to_level_3(self, request, queryset):
        queryset.update(level=3)

    def change_to_level_2(self, request, queryset):
        queryset.update(level=2)

    def change_to_level_1(self, request, queryset):
        queryset.update(level=1)

    def lesson_type(self, obj):
        return obj.LESSON_TYPE_CHOICES[obj.lesson_type][1]

admin.site.register(Lesson, LessonAdmin)


class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'user', 'created_at', 'updated_at')
    search_fields = ('user', )
    ordering = ('-created_at',)

admin.site.register(UserActivity, UserActivityAdmin)


class ActivityProgressAdmin(admin.ModelAdmin):
    list_display = ('activity', 'lesson', 'next_lesson', 'created_at', 'updated_at')
    search_fields = ('activity', 'lesson')
    ordering = ('-created_at',)

admin.site.register(ActivityProgress, ActivityProgressAdmin)

admin.site.register(LessonRating)
admin.site.register(UserActivityRating)
admin.site.register(UserActivityLike)

class LessonLikeAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'user', 'created_at', 'updated_at')
    search_fields = ('lesson', 'user')
    ordering = ('-created_at',)

admin.site.register(LessonLike , LessonLikeAdmin)

class ActivityTimelineAdmin(admin.ModelAdmin):
    list_display = ('activity', 'timeline', 'created_at', 'updated_at')

admin.site.register(ActivityTimeline, ActivityTimelineAdmin)


class LessonTimelineAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'timeline', 'created_at', 'updated_at')


admin.site.register(LessonTimeline, LessonTimelineAdmin)