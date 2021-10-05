import datetime as dt

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import (
    ManagerScheduleRegistForm, ManagerScheduleUpdateForm,
    StaffScheduleDayRegistForm, StaffScheduleUpdateForm
)
from .mixins import (
    MonthMixin, StaffApplicationScheduleMixin, StaffApprovedScheduleMixin,
    ManagerApplicationAllScheduleMixin, ManagerApprovedAllScheduleMixin
)
from .models import Schedule, Status
from staff.views import ManagerMixin


class ManagerApplicationAllSchedule(ManagerMixin, ManagerApplicationAllScheduleMixin, generic.TemplateView):
    """全スタッフのスケジュールを表示するView"""

    template_name = 'schedule/manager_all_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class ManagerApprovedAllSchedule(ManagerMixin, ManagerApprovedAllScheduleMixin, generic.TemplateView):
    """全スタッフのスケジュールを承認するView"""

    template_name = 'schedule/manager_all_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class ManagerScheduleRegistView(ManagerMixin, CreateView):
    """管理者がスケジュールを作成するView"""

    model = Schedule
    template_name = 'schedule/manager_schedule_regist.html'
    form_class = ManagerScheduleRegistForm
    success_url = reverse_lazy('schedule:manager_application')

    def form_valid(self, form):
        status = Status.objects.get(status='application')
        form.instance.status = status
        return super(ManagerScheduleRegistView, self).form_valid(form)


class ManagerScheduleDetailView(LoginRequiredMixin, DetailView):
    """管理者がスケジュールの詳細をみるView"""

    model = Schedule
    template_name = 'schedule/manager_schedule_detail.html'


class ManagerScheduleDeleteView(LoginRequiredMixin, DeleteView, MonthMixin):
    """管理者がスケジュールを削除するView"""

    model = Schedule
    template_name = 'schedule/manager_schedule_delete.html'
    success_url = reverse_lazy('schedule:manager_application')


class ManagerScheduleUpdateView(LoginRequiredMixin, UpdateView, MonthMixin):
    """管理者がスケジュールを更新するView"""

    model = Schedule
    template_name = 'schedule/manager_schedule_update.html'
    form_class = ManagerScheduleUpdateForm

    def get_success_url(self):
        return reverse_lazy('schedule:manager_application')


class StaffApplicationSchedule(LoginRequiredMixin, StaffApplicationScheduleMixin, generic.TemplateView):
    """ログインしているスタッフの申請中スケジュールを表示するView"""

    template_name = 'schedule/staff_application_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class StaffApprovedSchedule(LoginRequiredMixin, StaffApprovedScheduleMixin, generic.TemplateView):
    """ログインしているスタッフの承認済みスケジュールを表示するView"""

    template_name = 'schedule/staff_approved_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class StaffScheduleDetailView(LoginRequiredMixin, DetailView):
    """スタッフがスケジュールの詳細をみるView"""

    model = Schedule
    template_name = 'schedule/staff_schedule_detail.html'


class StaffScheduleDeleteView(LoginRequiredMixin, DeleteView, MonthMixin):
    """スタッフがスケジュールを削除するView"""

    model = Schedule
    template_name = 'schedule/staff_schedule_delete.html'
    success_url = reverse_lazy('schedule:staff_application_schedule')


class StaffScheduleDayRegistView(LoginRequiredMixin, CreateView, MonthMixin):
    """スタッフが日付からスケジュールを作成するView"""

    model = Schedule
    template_name = 'schedule/staff_schedule_day_regist.html'
    form_class = StaffScheduleDayRegistForm
    success_url = reverse_lazy('schedule:staff_application_schedule')

    def get_form_kwargs(self):
        """URLから日付を取得"""
        kwargs = super(StaffScheduleDayRegistView, self).get_form_kwargs()
        date = dt.datetime.strptime(
            str(self.kwargs["year"]) + "/" + str(self.kwargs["month"]) + "/" + str(self.kwargs["day"]), '%Y/%m/%d'
        )
        kwargs['date'] = date
        return kwargs

    def form_valid(self, form):
        form.instance.staff = self.request.user
        status = Status.objects.get(status='application')
        form.instance.status = status
        return super(StaffScheduleDayRegistView, self).form_valid(form)


class StaffScheduleUpdateView(LoginRequiredMixin, UpdateView, MonthMixin):
    """スタッフがスケジュールを更新するView"""

    model = Schedule
    template_name = 'schedule/staff_schedule_update.html'
    form_class = StaffScheduleUpdateForm

    def get_success_url(self):
        return reverse_lazy('schedule:staff_application_schedule')

