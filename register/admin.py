from django.contrib import admin
from .models import Integrante, ObjectiveKeyResult

# Register your models here.
class ObjectiveKeyResultInLine(admin.StackedInline):
    model = ObjectiveKeyResult
    extra = 1

class IntegranteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Nome',          {"fields": ('nome',),}),
    )
    inlines = [ObjectiveKeyResultInLine]

admin.site.register(Integrante, IntegranteAdmin)
