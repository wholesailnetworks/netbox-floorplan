from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name='svg'),
]
