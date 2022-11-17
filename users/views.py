from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import Users

@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def user_detail(request, id):
    ...

@api_view(http_method_names=['GET', 'POST'])
def user_list(request):
    ...
    
 