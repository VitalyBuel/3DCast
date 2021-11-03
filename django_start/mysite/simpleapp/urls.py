from django.urls import path
from .views import ProductList, ProductDetail  # импортируем наше представление

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view()),
]
