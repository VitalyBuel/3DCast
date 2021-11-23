from django.urls import path
from .views import index, detail

urlpatterns = [
    path('news/', index, name='index'),
<<<<<<< HEAD
    path('news/<int:pk>', detail, name='detail')
=======
    path('news/<int:pk>/', detail, name='detail'),
>>>>>>> 4c0ec9193bc7e3f3fbbc097d6ec02758360cad75
]