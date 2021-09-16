import datetime as dt

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import StaffScheduleRegistForm, StaffScheduleDayRegistForm, StaffScheduleUpdateForm
from .mixins import StaffScheduleMixin, ManagerAllScheduleMixin
from .models import Schedule
from staff.views import ManagerMixin


class ManagerAllSchedule(ManagerMixin, ManagerAllScheduleMixin, generic.TemplateView):
    """全スタッフのスケジュールを表示するView"""

    template_name = 'schedule/manager_all_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class StaffSchedule(LoginRequiredMixin, StaffScheduleMixin, generic.TemplateView):
    """ログインしているスタッフのスケジュールを表示するView"""

    template_name = 'schedule/staff_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class StaffScheduleDeleteView(LoginRequiredMixin, DeleteView):
    """スタッフがスケジュールを削除するView"""

    model = Schedule
    template_name = 'schedule/staff_schedule_delete.html'
    success_url = reverse_lazy('schedule:staff_schedule')


class StaffScheduleRegistView(LoginRequiredMixin, CreateView):
    """スタッフが日付を指定してスケジュールを作成するView"""

    template_name = 'schedule/staff_schedule_regist.html'
    form_class = StaffScheduleRegistForm
    success_url = reverse_lazy('schedule:staff_schedule')

    def form_valid(self, form):
        form.instance.staff = self.request.user
        return super(StaffScheduleRegistView, self).form_valid(form)


class StaffScheduleDayRegistView(LoginRequiredMixin, CreateView):
    """スタッフが日付からスケジュールを作成するView"""

    model = Schedule
    template_name = 'schedule/staff_schedule_day_regist.html'
    form_class = StaffScheduleDayRegistForm
    success_url = reverse_lazy('schedule:staff_schedule')

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
        return super(StaffScheduleDayRegistView, self).form_valid(form)


class StaffScheduleUpdateView(LoginRequiredMixin, UpdateView):
    """スタッフがスケジュールを更新するView"""

    model = Schedule
    template_name = 'schedule/staff_schedule_update.html'
    form_class = StaffScheduleUpdateForm

    def get_success_url(self):
        return reverse_lazy('schedule:staff_schedule')
