from django.contrib import admin
from .models import *


# For Question List View
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date',)
    search_fields = ['question_text', 'pub_date',]
    list_filter = ('question_text', 'pub_date',);
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
