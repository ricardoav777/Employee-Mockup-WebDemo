import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from webdemo_app.forms import EmployeeForm
from webdemo_app.models import Employee
# Create your views here.


class EmployeeListView(ListView):
    model = Employee
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['queryset'] = Employee.objects.all()
        return context


class EmployeeCreateView(CreateView):
    model = Employee
    success_url = reverse_lazy('employee-list')
    fields = ['first_name', 'last_name','email']


class EmployeeUpdateView(UpdateView):
    model = Employee
    success_url = reverse_lazy('employee-list')
    fields = ['first_name', 'last_name','email']


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('employee-list')


def multiple_delete(request):
    if request.method == "POST":
        data = request.POST.get('checked_array')
        if data:
            int_data = []
            for elem in json.loads(data):
                int_data.append(elem)
            try:
                context = {}
                qs = Employee.objects.filter(pk__in=int_data)
            except Employee.DoesNotExist:
                return JsonResponse(status=404)
            qs._raw_delete(qs.db)
            context = {}
            context['queryset'] = Employee.objects.all()
            return render(request, 'webdemo_app/employee_list.html', context)
        else:
            return JsonResponse(status=404)
    elif request.method == "GET":
        context = {}
        context['queryset'] = Employee.objects.all()
        return render(request, 'webdemo_app/employee_list.html', context)

    else:
        return HttpResponse(status=405)


def employee_search(request):
    if request.method == "GET":
        try:
            name = request.GET.get('first_name')
            context = {}
            context['queryset'] = Employee.objects.filter(first_name__icontains=name)
            return render(request, 'webdemo_app/employee_list.html', context)
        except Exception as e:
            return HttpResponse(status=500, message="Error interno, por favor intente de nuevo")


