from django.contrib import admin
from .models import Stage, Grade, Class, Student


# registering models to be shown in the admin page
admin.site.register(Stage)
admin.site.register(Grade)
admin.site.register(Class)
admin.site.register(Student)
