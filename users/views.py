from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import User, Address
from users.serializers import UserSerializer, AddressSerializer

@api_view(http_method_names=['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        objects = User.objects.all()
        serializer = UserSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def user_detail(request, id):
    object = get_object_or_404(User, id=id)
    if request.method == 'GET':
        serializer = UserSerializer(object)
        return JsonResponse(serializer.data)
    if request.method == 'PATCH':
        serializer = UserSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=204)
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
            object.delete()
            return Response(status=204)
        
@api_view(http_method_names=['GET', 'POST'])    
def address_list(request, id, address_id):
    #object = get_object_or_404(User, id=id)
    if request.method == 'GET':
        objects = Address.objects.all()
        serializer = AddressSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(http_method_names=['GET', 'PATCH', 'DELETE'])
def address_detail(request, id):
    object = get_object_or_404(Address, id=id)
    if request.method == 'GET':
        serializer = AddressSerializer(object)
        return JsonResponse(serializer.data)
    if request.method == 'PATCH':
        serializer = AddressSerializer(object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=204)
        return JsonResponse(serializer.errors, status=400)
    if request.method == 'DELETE':
            object.delete()
            return Response(status=204)
