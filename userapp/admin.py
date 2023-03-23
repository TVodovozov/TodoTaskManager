from django.contrib import admin

from todoapp.models import Project, ToDo
from userapp.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Project)
admin.site.register(ToDo)
