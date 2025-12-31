from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Admin configuration for Student model."""
    
    list_display = ('full_name', 'university_id', 'age', 'date_of_birth', 'salary', 'created_at')
    list_filter = ('age', 'created_at')
    search_fields = ('full_name', 'university_id', 'address')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'university_id', 'photo')
        }),
        ('Demographics', {
            'fields': ('age', 'date_of_birth', 'address')
        }),
        ('Financial', {
            'fields': ('salary',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
