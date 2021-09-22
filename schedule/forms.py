from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Schedule


class ManagerScheduleRegistForm(forms.ModelForm):
    """管理者がスケジュールを作成するフォーム
    statusの初期値はapplication
    """

    class Meta:
        model = Schedule
        fields = ('date', 'staff', 'shift_name',)

    def save(self, commit=False):
        schedule = super().save(commit=False)
        schedule.save()
        return schedule


class ManagerScheduleUpdateForm(forms.ModelForm):
    """管理者がスケジュールを更新するフォーム
    statusの初期値はapplication
    """

    class Meta:
        model = Schedule
        fields = ('shift_name',)

    def save(self, commit=False):
        schedule = super().save(commit=False)
        schedule.save()
        return schedule


class StaffScheduleDayRegistForm(forms.ModelForm):
    """スタッフが日付からスケジュールを作成するフォーム
    URLから日付を取得するためスタッフが入力する必要なし
    statusの初期値はapplication
    """

    class Meta:
        model = Schedule
        fields = ('date', 'shift_name',)

    def __init__(self, *args, **kwargs):
        """URLから日付を取得"""
        self.date = kwargs.pop('date')
        print(self.date)
        super(StaffScheduleDayRegistForm, self).__init__(*args, **kwargs)
        self.fields['date'].initial = self.date

    def save(self, commit=False):
        schedule = super().save(commit=False)
        schedule.save()
        return schedule


class StaffScheduleUpdateForm(forms.ModelForm):
    """スタッフがスケジュールを更新するフォーム
    statusの初期値はapplication
    """

    class Meta:
        model = Schedule
        fields = ('shift_name',)

    def save(self, commit=False):
        schedule = super().save(commit=False)
        schedule.save()
        return schedule
