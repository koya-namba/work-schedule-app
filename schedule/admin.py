from django.contrib import admin

from .models import Schedule, Shift


admin.site.register(Shift)
admin.site.register(Schedule)

