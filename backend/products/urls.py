from django.urls import path

import products.views as views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view()),
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
]
