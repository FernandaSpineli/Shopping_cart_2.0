from django.urls import path

from users.views import user_detail

urlpatterns = [
    #path('agendamentos/', agendamento_list),
    path('agendamentos/<int:id>/', user_detail)
]