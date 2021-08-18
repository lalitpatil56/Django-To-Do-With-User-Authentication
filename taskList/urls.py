from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', TodoLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', TodoRegister.as_view(), name="register"),
    path('', Tasks.as_view(), name="tasks"),
    path('task-detail/<int:pk>/', TaskDetails.as_view(), name="task-detail"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name="task-delete"),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
]
