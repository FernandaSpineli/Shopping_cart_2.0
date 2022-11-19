from django.urls import path

# from users.views import user_detail, user_list, address_detail, address_list
from users import views

urlpatterns = [
    path('usuarios/', views.user_list),
    path('usuarios/<int:id>/', views.user_detail),
    path('usuarios/<int:id>/addresses/', views.address_list),
    path('usuarios/<int:id>/addresses/', views.address_detail)
]