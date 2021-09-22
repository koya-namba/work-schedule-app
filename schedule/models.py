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


class Status(models.Model):
    """スケジュールが申請中か承認済か確認するモデル"""
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.status


class Schedule(models.Model):
    """スケジュールの詳細に関するモデル"""

    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    shift_name = models.ForeignKey(Shift, on_delete=models.CASCADE, related_name='シフト名')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='状態')

    def __str__(self):
        return f'{self.date}'

    class Meta:
        unique_together = [['staff', 'date']]
