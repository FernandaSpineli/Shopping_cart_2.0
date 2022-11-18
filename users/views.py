from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User
from users.serializers import UserSerializer

@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def user_detail(request, id):
    object = get_object_or_404(User, id=id)
    if request.method == 'GET':
        serializer = UserSerializer(object)
        return JsonResponse(serializer.data)
        
@api_view(http_method_names=['GET', 'POST'])
def user_list(request):
    ...
    
 