from django.urls import path

# from users.views import user_detail, user_list, address_detail, address_list
from users import views

urlpatterns = [
    path('usuarios/', views.user_list),
    path('usuarios/<int:id>/', views.user_detail),
    path('enderecos/', views.address_list),
    path('enderecos/<int:id>/', views.address_detail)
]