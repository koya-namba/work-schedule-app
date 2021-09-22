from django.contrib import admin

from .models import Schedule, Shift, Status


admin.site.register(Shift)
admin.site.register(Status)
admin.site.register(Schedule)

