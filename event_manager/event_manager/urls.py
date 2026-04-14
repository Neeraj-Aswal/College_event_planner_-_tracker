from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('user/', include('user.urls')),
    path('student/', include('student.urls')),
    path('organizer/', include('organizer.urls')),
]
