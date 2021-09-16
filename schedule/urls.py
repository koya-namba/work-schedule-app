from django.urls import path
from .views import (
    ManagerAllSchedule, StaffSchedule, StaffScheduleDeleteView, StaffScheduleRegistView,
    StaffScheduleDayRegistView, StaffScheduleUpdateView
)

app_name = 'schedule'

urlpatterns = [
    # 管理者のURL
    path('manager_all_schedule/', ManagerAllSchedule.as_view(), name='manager_all_schedule'),
    path('manager_all_schedule/<int:year>/<int:month>/', ManagerAllSchedule.as_view(), name='manager_all_schedule'),

    # スタッフのURL
    path('staff_schedule/', StaffSchedule.as_view(), name='staff_schedule'),
    path('staff_schedule/<int:year>/<int:month>/', StaffSchedule.as_view(), name='staff_schedule'),
    path('staff_schedule_regist/', StaffScheduleRegistView.as_view(), name='staff_schedule_regist'),
    path(
        'staff_schedule_day_regist/<int:year>/<int:month>/<int:day>',
        StaffScheduleDayRegistView.as_view(), name='staff_schedule_day_regist'
    ),
    path('staff_schedule_update/<int:pk>/', StaffScheduleUpdateView.as_view(), name='staff_schedule_update'),
    path('staff_schedule_delete/<int:pk>/', StaffScheduleDeleteView.as_view(), name='staff_schedule_delete'),
]