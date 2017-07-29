from django.shortcuts import render
from rest_framework.generics import ListAPIView

from workout.models import Workout
from workout.serializers import WorkoutSerializer


class WorkoutListAPIView(ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer



