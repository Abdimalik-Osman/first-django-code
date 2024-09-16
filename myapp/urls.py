from django.urls import path
from . import views  # Import views from your app
urlpatterns = [
    path('', views.book_list, name='book_list'),  # URL pattern for the book list view
    path('<int:pk>/', views.book_detail, name='book_detail'),  # URL pattern for the book detail view
]
