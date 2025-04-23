from django.contrib import admin
from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'user', 'id')
    list_filter = ('completed', 'user')
    search_fields = ('title', 'user__username')
    list_per_page = 25