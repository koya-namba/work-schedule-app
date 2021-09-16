from django.db import models

from staff.models import User


class Shift(models.Model):
    """シフトの詳細に関するモデル"""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.name


class Schedule(models.Model):
    """スケジュールの詳細に関するモデル"""

    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    shift_name = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='シフト名')

    def __str__(self):
        return f'{self.date}'

    class Meta:
        unique_together = [['staff', 'date']]




