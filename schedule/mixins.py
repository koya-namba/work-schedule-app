import calendar
import datetime

from staff.models import User


class MonthMixin:
    """月に関する情報を提供するMixin"""

    def get_previous_month(self, date):
        """前月を返す"""
        if date.month == 1:
            return date.replace(year=date.year-1, month=12, day=1)
        else:
            return date.replace(month=date.month-1, day=1)

    def get_next_month(self, date):
        """次月を返す"""
        if date.month == 12:
            return date.replace(year=date.year+1, month=1, day=1)
        else:
            return date.replace(month=date.month+1, day=1)

    def get_month_days(self, date):
        """その月の全ての日を返す"""
        return [datetime.date(date.year, date.month, 1) + datetime.timedelta(days=i) for i in range(calendar.monthrange(date.year, date.month)[1])]

    def get_current_month(self):
        """現在の月を返す"""
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    def get_month_calendar(self):
        """月に関する情報の入った辞書を返す"""
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'month_days': self.get_month_days(current_month),
            'month_current': current_month,
            'month_previous': self.get_previous_month(current_month),
            'month_next': self.get_next_month(current_month),
        }
        return calendar_data


class ManagerAllScheduleMixin(MonthMixin):
    """スケジュール付きの、月の情報を提供するMixin"""

    def get_month_schedules(self, start, end, days, staff_list):
        """スタッフごとにそれぞれの日とスケジュールを返す"""
        lookup = {
            # date__range: (1日, 31日)'を動的に作る
            '{}__range'.format(self.date_field): (start, end),
        }
        staff_all_schedule = {}
        # Schedule.objects.filter(date__range=(1日, 31日), staff=staff)
        for staff in staff_list:
            queryset = self.model.objects.filter(**lookup, staff=staff)
            # {1日のdatetime: 1日のスケジュール, 2日のdatetime: 2日の...}の辞書を作る
            day_schedules = {day: [] for day in days}

            for schedule in queryset:
                schedule_date = getattr(schedule, self.date_field)
                day_schedules[schedule_date].append(schedule)

            staff_all_schedule[staff] = day_schedules

        return staff_all_schedule

    def get_month_calendar(self):
        """その月に関する情報とスタッフのリストを返す"""
        calendar_context = super().get_month_calendar()
        month_days = calendar_context['month_days']
        month_first = month_days[0]
        month_last = month_days[-1]
        staff_list = User.objects.all().order_by('employee_id')
        calendar_context['month_day_schedules'] = self.get_month_schedules(
            month_first,
            month_last,
            month_days,
            staff_list
        )
        return calendar_context


class StaffScheduleMixin(MonthMixin):
    """ログインしているスタッフのスケジュール付きの、月の情報を提供するMixin"""

    def get_month_schedules(self, start, end, days, staff):
        """それぞれの日とスケジュールを返す"""
        lookup = {
            # date__range: (1日, 31日)'を動的に作る
            '{}__range'.format(self.date_field): (start, end),
        }
        # Schedule.objects.filter(date__range=(1日, 31日), staff=staff)
        queryset = self.model.objects.filter(**lookup, staff=staff)
        # {1日のdatetime: 1日のスケジュール, 2日のdatetime: 2日の...}の辞書を作る
        day_schedules = {day: [] for day in days}

        for schedule in queryset:
            schedule_date = getattr(schedule, self.date_field)
            day_schedules[schedule_date].append(schedule)

        return day_schedules

    def get_month_calendar(self):
        """その月に関する情報とログインしているスタッフを返す"""
        calendar_context = super().get_month_calendar()
        month_days = calendar_context['month_days']
        month_first = month_days[0]
        month_last = month_days[-1]
        staff = self.request.user
        calendar_context['month_day_schedules'] = self.get_month_schedules(
            month_first,
            month_last,
            month_days,
            staff
        )
        return calendar_context
