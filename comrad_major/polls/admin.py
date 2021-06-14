from django.contrib import admin

from .models import PollQuestion, PollChoice


# Register your models here.

class PollChoiceInline(admin.TabularInline):
    model = PollChoice
    extra = 3


class PollChoiceAdmin(admin.ModelAdmin):
    pass


class PollQuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [PollChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(PollQuestion, PollQuestionAdmin)
admin.site.register(PollChoice)
