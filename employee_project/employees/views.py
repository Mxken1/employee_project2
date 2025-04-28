from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from django.db.models import Q
# แสดงรายชื่อพนักงาน
def employee_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        employees = Employee.objects.filter(
            Q(name__icontains=search_query) |
            Q(position__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    else:
        employees = Employee.objects.all()
    
    context = {'employees': employees}
    return render(request, 'employees/employee_list.html', context)


# เพิ่มพนักงาน
def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        position = request.POST.get('position')
        email = request.POST.get('email')

        # เช็คข้อมูลนิดหน่อย
        if name and position and email:
            Employee.objects.create(name=name, position=position, email=email)
            return redirect('employee_list')
        
    return render(request, 'employees/add_employee.html')

# แก้ไขพนักงาน
def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    
    if request.method == 'POST':
        employee.name = request.POST.get('name', employee.name)
        employee.position = request.POST.get('position', employee.position)
        employee.email = request.POST.get('email', employee.email)
        employee.save()
        return redirect('employee_list')
    
    context = {'employee': employee}
    return render(request, 'employees/edit_employee.html', context)

# ลบพนักงาน
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    employee.delete()
    return redirect('employee_list')
