from django.contrib import admin
from profiles import models

admin.site.register(models.StudentProfile)
admin.site.register(models.TeacherProfile)
admin.site.register(models.Institute)
