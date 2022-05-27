from django.urls import path

from webdemo_app.views import EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, multiple_delete

urlpatterns = [
    path('create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('<pk>/update', EmployeeUpdateView.as_view(), name='employee-update'),
    path('<pk>/delete/', EmployeeDeleteView.as_view(),name='employee-delete'),
    path('', multiple_delete, name='employee-list'),
]
