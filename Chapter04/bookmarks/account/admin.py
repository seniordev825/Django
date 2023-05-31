from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['date_of_birth', 'photo','password']
    raw_id_fields = []
