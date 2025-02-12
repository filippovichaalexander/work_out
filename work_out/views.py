# from http.client import responses
#
# from django.core.signing import JSONSerializer
# from django.http import JsonResponse
# from django.shortcuts import render
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from work_out.serializer import UserSerializer
from .models import User, TrainerProfile, TrainingPlan, Exercise, TrainingSession, ExerciseResult, Notification, Review, \
    JournalEntry
from .serializer import (
    UserSerializer,
    TrainerProfileSerializer,
    TrainingPlanSerializer,
    ExerciseSerializer,
    TrainingSessionSerializer,
    ExerciseResultSerializer,
    NotificationSerializer,
    ReviewSerializer,
    JournalEntrySerializer,
)


# from .models import TrainingPlans

# from .serializer import TrainingPlansSerializer


# Without DRF
# def training_plans(request):
#     if request.method == 'GET':
#         tps = TrainingPlans.objects.all()
#         serializer = TrainingPlansSerializer(tps, many=True)
#         return JsonResponse(serializer.data, safe=False)


# Using DRF
# getting, updateing, deleting the object
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def api_training_detail(request, pk):
#     training_plan = TrainingPlans.objects.get(id=pk)
#
#     if request.method == 'GET':
#         serializer = TrainingPlansSerializer(training_plan)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = TrainingPlansSerializer(training_plan, request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.errors, status.HTTP_200_OK)
#
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         training_plan.delete()
#         return Response(status.HTTP_200_OK)


# Create new training plans
# @api_view(['POST'])
# def create_training_plan(request):
#     if request.method == 'POST':
#         serializer = TrainingPlansSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()  # Create new instance
#             return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created instance data
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Using classes
# class APITrainingPlans(APIView):
#     def get(self, request):
#         tps = TrainingPlans.objects.all()
#         serializer = TrainingPlansSerializer(tps, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TrainingPlansSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# class APITrainingPlan(APIView):
#     def get(self, request, pk):
#         training_plan = TrainingPlans.objects.get(id=pk)
#         serializer = TrainingPlansSerializer(training_plan, request.data)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         training_plan = TrainingPlans.objects.get(id=pk)
#         serializer = TrainingPlansSerializer(training_plan, request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         training_plan = TrainingPlans.objects.get(id=pk)
#         training_plan.delete()
#         return Response(status=status.HTTP_200_OK)

# Using generic
# class APITrainingPlansGeneric(ListCreateAPIView):
#     queryset = TrainingPlans.objects.all()
#     serializer_class = TrainingPlansSerializer

# class APITrainingPlansDetailGeneric(RetrieveUpdateDestroyAPIView):
#     queryset = TrainingPlans.objects.all()
#     serializer_class = TrainingPlansSerializer

# Using ModelViewSet
# class APITrainingPlanViewSet(ModelViewSet):
#     queryset = TrainingPlans.objects.all()
#     serializer_class = TrainingPlansSerializer

# User viewset
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['create', 'list']:
            return [AllowAny()]
        return [IsAuthenticated()]


# Trainer Profile Viewset
class TrainerProfileViewSet(ReadOnlyModelViewSet):
    queryset = TrainerProfile.objects.all()
    serializer_class = TrainerProfileSerializer
    permission_classes = [AllowAny]

# Training Plan ViewSet
class TrainingPlanViewSet(ModelViewSet):
    queryset = TrainingPlan.objects.all()
    serializer_class = TrainingPlanSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        # Set the current user as the owner of the plan
        serializer.save(user=self.request.user)

# Excercise ViewSet
class ExcerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

# Training Session ViewSet
class TrainingSessionViewSet(ModelViewSet):
    queryset = TrainingSession.objects.all()
    serializer_class = TrainingSessionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Set the current user as the owner of the session
        serializer.save(user=self.request.user)

# Excercise
class ExcerciseResultViewSet(ModelViewSet):
    queryset = ExerciseResult.objects.all()
    serializer_class = ExerciseResultSerializer
    permission_classes = [IsAuthenticated]
