#  Concept 1
# from django.db import models
#
# class TrainingPlans(models.Model):
#     name = models.CharField(max_length=200, null=False)
#     level = models.CharField(max_length=200, null=False)
#     number_of_sets = models.FloatField()

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('user', 'User'),
        ('trainer', 'Trainer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')


class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='trainer_profile')
    bio = models.TextField(blank=True)
    experience = models.PositiveIntegerField(help_text="Years of experience", default=0)
    rating = models.FloatField(default=0.0)


class TrainingPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_plans')
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_plans')
    created_at = models.DateTimeField(auto_now_add=True)


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, related_name='exercises')
    sets = models.PositiveIntegerField(default=1)
    repetitions = models.PositiveIntegerField(default=10)
    weight = models.FloatField(default=0.0, help_text="Weight in kg")


class TrainingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='training_sessions')
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, related_name='sessions')
    date = models.DateField()
    notes = models.TextField(blank=True)


class ExerciseResult(models.Model):
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE, related_name='exercise_results')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='results')
    sets_completed = models.PositiveIntegerField(default=0)
    repetitions_completed = models.PositiveIntegerField(default=0)
    weight_used = models.FloatField(default=0.0)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_for = models.DateTimeField()


class Review(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    trainer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='trainer_reviews')
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, null=True, blank=True, related_name='plan_reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)