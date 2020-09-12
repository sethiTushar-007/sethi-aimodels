from django.urls import path
from . import views

urlpatterns = [
    path('',views.facemask_detection,name='facemask_detection'),
    path('predict',views.predict,name='facemask_predict'),
]
