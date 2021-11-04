from django.urls import path
from .views import index

urlpatterns = [
    path('newapp_list/', index)
]