from django.urls import path

from users.views import user_detail, user_list

urlpatterns = [
    path('usuarios/', user_list),
    path('usuarios/<int:id>/', user_detail)
]