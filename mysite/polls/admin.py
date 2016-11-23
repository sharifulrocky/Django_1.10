from django.contrib import admin
from .models import *


def make_published(self, request, queryset):
    row_update = queryset.update(status='p')
    if row_update == 1:
        message = '1 row was selected'
    else:
        message = '%s were selected.' % row_update
    self.message_user(request, '%s Published' % message)

make_published.short_description = "Mark selected Questions as published"


def make_withdrawn(self, request, queryset):
    row_update = queryset.update(status='w')
    if row_update == 1:
        message = '1 row was selected'
    else:
        message = '%s were selected.' % row_update
    self.message_user(request, '%s Withdrawn' % message)

make_withdrawn.short_description = "Mark selected stories as Withdrawn"


# For Question List View
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'status')
    search_fields = ['question_text', 'pub_date', 'status']
    list_filter = ('question_text', 'pub_date', 'status')
    actions = [make_published, make_withdrawn]
    fieldsets = (
        ("General Information", {
            "fields": ("question_text", "pub_date",)
        }),
        ("Social Media", {
            "classes": ("collapse",),
            "fields": ("twitter", "facebook",),
            "description": "Add social media here"
        })
    )


# Register Question Model
admin.site.register(Question, QuestionAdmin)


# For Choice List View
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    # Can't add primary key field in search_fields list
    search_fields = ['choice_text', 'votes']
    list_filter = ('question', 'choice_text', 'votes')


# Register Choice Model
admin.site.register(Choice, ChoiceAdmin)
