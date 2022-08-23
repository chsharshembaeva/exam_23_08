from django.contrib import admin
from .models import *

admin.site.register(Language)
admin.site.register(Student)


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'main_work', 'phone_number', 'level')

    @admin.display(description='Level')
    def level(self, obj):
        if 2022 - obj.experience.year > 3:
            return 'middle'
        else:
            return 'strong junior'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_filter = ('language', 'mentor')
    list_displays = ('name', 'date_started', 'mentor__name', 'student__name', 'language')
    search_fields = ('mentor__name', 'student_name')