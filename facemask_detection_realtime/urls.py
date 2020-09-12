from django.urls import path
from . import views

urlpatterns = [
    path('',views.facemask_detection_realtime,name='facemask_detection'),
]
