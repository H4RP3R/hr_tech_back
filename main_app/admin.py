from django.contrib import admin

from main_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
