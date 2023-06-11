from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
    path('floorplans/test/', views.TestView.as_view(), name='svg'),
    path('floorplans/', views.FloorplanListView.as_view(), name='floorplan_list'),
    path('floorplans/add/', views.FloorplanEditView.as_view(), name='floorplan_add'),
    path('floorplans/<int:pk>/', views.FloorplanView.as_view(), name='floorplan'),
    path('floorplans/<int:pk>/edit/', views.FloorplanMapEditView.as_view(), name='floorplan_edit'),
    path('floorplans/<int:pk>/delete/', views.FloorplanDeleteView.as_view(), name='floorplan_delete'),
    path('floorplans/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='floorplan_changelog', kwargs={'model': models.Floorplan})
)