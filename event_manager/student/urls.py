from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='student_dashboard'),
    path('events/', views.event_list, name='student_events'),
    path('events/<int:id>/', views.event_detail, name='event_detail'),
    path('join/<int:id>/', views.join_event, name='join_event'), 
    path('my-events/', views.my_events, name='my_events'),
]