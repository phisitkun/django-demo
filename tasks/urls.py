from django.urls import path
from .views import list_tasks, create_task

urlpatterns = [
    path('', list_tasks),
    path('new_task/', create_task, name='create_task'),
]