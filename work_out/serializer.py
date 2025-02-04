from rest_framework import serializers

from .models import TrainingPlans

class TrainingPlansSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    level = serializers.CharField(max_length=200)
    number_of_sets = serializers.FloatField()

    def create(self, validated_data):
        return TrainingPlans.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.level = validated_data.get('level', instance.level)
        instance.number_of_sets = validated_data.get('number_of_sets', instance.number_of_sets)
        instance.save()
        return instance

# ModelSerializer
# class TrainingPlansSerializer(serializers.Serializer):
#     class Meta:
#         model = TrainingPlans
#         fields = ['id', 'name', 'level', 'number_of_sets']
