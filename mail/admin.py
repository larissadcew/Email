# admin.py
from django.contrib import admin
from .models import User, Email

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active')
    search_fields = ('username', 'email')
    filter_horizontal = ('emails', 'emails_sent', 'emails_received')


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sender', 'get_recipients', 'timestamp', 'read', 'archived')
    search_fields = ('subject', 'body', 'sender__username', 'recipients__username')
    list_filter = ('read', 'archived', 'timestamp')

    def get_recipients(self, obj):
        return ", ".join([user.username for user in obj.recipients.all()])
    get_recipients.short_description = 'Destinatários'