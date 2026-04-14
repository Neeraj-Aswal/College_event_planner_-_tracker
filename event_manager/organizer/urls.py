from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='organizer_dashboard'),
    path('create/', views.create_event, name='create_event'),
    path('my-events/', views.my_events, name='my_events'),
    path('edit/<int:id>/', views.edit_event, name='edit_event'),
    path('delete/<int:id>/', views.delete_event, name='delete_event'),
]