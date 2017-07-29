from rest_framework import serializers

from workout.models import Workout
from member.models import MyUser


class WorkoutSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Workout
        fields = [
            'id',
            'name',
            'user',
        ]
