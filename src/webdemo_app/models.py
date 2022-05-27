import re
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

email_reg = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


class Employee(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    email = models.EmailField(validators=[ RegexValidator(
        regex=email_reg, message='Wrong email', code='invalid_username')])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"