from django.forms import ModelForm
from webdemo_app.models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        pass
