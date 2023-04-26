from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.TaskListView.as_view(), name='cbvname'),
    path('cbvdetails/<int:pk>/', views.TaskDetails.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.TaskUpdate.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDelete.as_view(), name='cbvdelete')
    ]