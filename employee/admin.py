from django.contrib import admin

from employee.models import Unit, Employee


@admin.register(Unit)
class AdminUnit(admin.ModelAdmin):
    list_display = ('name', 'parent')
    ordering = ('name', 'parent',)


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'unit', 'position', 'salary')
    ordering = ('unit', 'last_name', 'first_name', 'middle_name', 'position',)
    list_filter = ['unit']
    exclude = ['full_name']
