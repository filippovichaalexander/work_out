# Concept 1
# from rest_framework import serializers
#
# from .models import TrainingPlans
#
# class TrainingPlansSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=200)
#     level = serializers.CharField(max_length=200)
#     number_of_sets = serializers.FloatField()
#
#     def create(self, validated_data):
#         return TrainingPlans.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.level = validated_data.get('level', instance.level)
#         instance.number_of_sets = validated_data.get('number_of_sets', instance.number_of_sets)
#         instance.save()
#         return instance

# ModelSerializer
# class TrainingPlansSerializer(serializers.Serializer):
#     class Meta:
#         model = TrainingPlans
#         fields = ['id', 'name', 'level', 'number_of_sets']
# Concept 1

from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Exercise, ExerciseResult, JournalEntry, Notification, Review, TrainerProfile, TrainingPlan, TrainingSession

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'first_name', 'last_name']
        read_only_fields = ['role']


class TrainerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TrainerProfile
        fields = ['user', 'bio', 'experience', 'rating']


class TrainingPlanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    trainer = UserSerializer(read_only=True)

    class Meta:
        model = TrainingPlan
        fields = ['id', 'name', 'description', 'user', 'trainer', 'created_at']


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'training_plan', 'sets', 'repetitions', 'weight']


class TrainingSessionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    training_plan = TrainingPlanSerializer(read_only=True)

    class Meta:
        model = TrainingSession
        fields = ['id', 'user', 'training_plan', 'date', 'notes']


class ExerciseResultSerializer(serializers.ModelSerializer):
    session = TrainingSessionSerializer(read_only=True)
    exercise = ExerciseSerializer(read_only=True)

    class Meta:
        model = ExerciseResult
        fields = ['id', 'session', 'exercise', 'sets_completed', 'repetitions_completed', 'weight_used']


class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'is_read', 'created_at', 'scheduled_for']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    trainer = TrainerProfileSerializer(read_only=True)
    training_plan = TrainingPlanSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'trainer', 'training_plan', 'rating', 'comment', 'created_at']


class JournalEntrySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = JournalEntry
        fields = ['id', 'user', 'content', 'created_at']