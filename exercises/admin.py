from django.contrib import admin
from exercises.models import Exercise
from exercises.models import Discipline
from exercises.models import ExoAlias
from django.utils.encoding import python_2_unicode_compatible


class ExerciseAdmin(admin.ModelAdmin):
    readonly_fields = ('discipline', 'exo_number',)
    list_display = ('discipline', 'exo_number', 'title', 'is_published',)
    ordering = ('discipline', 'exo_number', )
    list_filter = ('discipline', 'exo_number', )


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Discipline)
admin.site.register(ExoAlias)
