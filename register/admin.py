from django.contrib import admin
from .models import Integrante, ObjectiveKeyResult

# Register your models here.
class IntegranteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Nome',          {"fields": ('nome',),}),
    )

admin.site.register(Integrante, IntegranteAdmin)
admin.site.register(ObjectiveKeyResult)
