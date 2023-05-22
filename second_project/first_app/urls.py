from django.urls import path
from . import views

urlpatterns = [
    path('info/',views.info),
    path('house/',views.house),
]