from django.db import models

from member.models import MyUser


class Workout(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(MyUser)
    img_workout = models.ImageField(upload_to='workout', blank=True)

    def __str__(self):
        return self.name


