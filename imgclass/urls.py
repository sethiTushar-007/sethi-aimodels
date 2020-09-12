from django.urls import path
from . import views

urlpatterns = [
    path('',views.imgclass,name='imgclass'),
    path('predict',views.predict,name='imgclass_predict'),
]
