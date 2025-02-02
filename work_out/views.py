from http.client import responses

from django.core.signing import JSONSerializer
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import TrainingPlans

from .serializer import TrainingPlansSerializer

# Without DRF
def training_plans(request):
    if request.method == 'GET':
        tps = TrainingPlans.objects.all()
        serializer = TrainingPlansSerializer(tps, many=True)
        return JsonResponse(serializer.data, safe=False)

# Using DRF
# getting, updateing, deleting the object
@api_view(['GET', 'PUT', 'DELETE'])
def api_training_detail(request, pk):
    training_plan = TrainingPlans.objects.get(id=pk)

    if request.method =='GET':
        serializer = TrainingPlansSerializer(training_plan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TrainingPlansSerializer(training_plan, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status.HTTP_200_OK)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        training_plan.delete()
        return Response(status.HTTP_200_OK)