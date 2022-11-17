from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from users.models import Users

# Create your views here.
def user_detail(request, id):
    obj = get_object_or_404(Users, id=id)
    return JsonResponse(obj.data)