"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from work_out import views

from rest_framework.routers import DefaultRouter


from work_out.views import (
    UserViewSet,
    TrainerProfileViewSet,
    ExcerciseViewSet,
    TrainingPlanViewSet,
    TrainingSessionViewSet,
    ExcerciseResultViewSet
)

router = DefaultRouter()
# router.register('training_plans', views.APITrainingPlanViewSet)

router.register('users', views.UserViewSet, basename='user' )
router.register('trainer-profiles', TrainerProfileViewSet, basename='trainingprofile')
router.register('trainer-plan', TrainingPlanViewSet, basename='trainingplan')
router.register('exercises', ExcerciseViewSet, basename='exercise')
router.register('training-session', TrainingSessionViewSet, basename='trainingsession')
router.register('exercise-results', ExcerciseResultViewSet, basename='exerciseresult')



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.training_plans),
    # path('training_plan/', views.create_training_plan),  # New endpoint for creating
    # path('training_plan/<int:pk>', views.api_training_detail),
    # path('training_plans/', views.APITrainingPlans.as_view()),
    # path('training_plan/<int:pk>', views.APITrainingPlan.as_view()),
    # path('training_plans/', views.APITrainingPlansGeneric.as_view()),
    # path('training_plan/<int:pk>', views.APITrainingPlansDetailGeneric.as_view()),
    path('api/', include(router.urls))

]
