import json


from django.http import JsonResponse
from django.shortcuts import render

from employee.models import Unit, Employee


def index(request):
    units = Unit.objects.all()
    return render(request, 'index.html', {'nodes': units})


def get_employees(request):
    unit_id = json.loads(request.body.decode("utf-8"))['unit_id']
    employees = list(Employee.objects.filter(unit_id=unit_id).order_by('last_name', 'first_name', 'middle_name').
                     values('full_name', 'position', 'employment_date', 'salary', 'unit__name'))
    return JsonResponse(employees, safe=False)

