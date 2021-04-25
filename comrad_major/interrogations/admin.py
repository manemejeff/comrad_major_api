from django.contrib import admin
from .models import Interrogation

# Register your models here.

class InterrogationAdmin(admin.ModelAdmin):
    model = Interrogation

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['date_start']
        else:
            return []

admin.site.register(Interrogation, InterrogationAdmin)
