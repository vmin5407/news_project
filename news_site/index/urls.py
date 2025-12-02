from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('category/<int:pk>/', views.category_page),
    path('news/<int:pk>/', views.news_page),
    path('saved', views.saved_page),
    path('add-to-saved/<int:n_id>', views.add_to_saved),
    path('delete-from-saved/<int:pk>', views.delete_from_saved),
    path('create', views.create),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
]
