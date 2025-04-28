from django.contrib import admin
from .models import Employee  # import โมเดลที่สร้างไว้

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'department', 'email', 'phone')  # คอลัมน์ที่โชว์ในหน้า admin
    search_fields = ('name', 'position', 'department')  # สามารถค้นหาได้ตาม name, position, department
    list_filter = ('department', 'position')  # มีตัวกรองตามแผนก และตำแหน่ง
