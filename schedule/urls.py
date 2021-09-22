from django.urls import path
from .views import (
    ManagerApplicationAllSchedule, ManagerApprovedAllSchedule, ManagerScheduleRegistView,
    ManagerScheduleDetailView, ManagerScheduleDeleteView, ManagerScheduleUpdateView,
    StaffApplicationSchedule, StaffApprovedSchedule, StaffScheduleDetailView, StaffScheduleDeleteView,
    StaffScheduleDayRegistView, StaffScheduleUpdateView
)

app_name = 'schedule'

urlpatterns = [
    # 管理者のURL
    path('manager_approved/', ManagerApprovedAllSchedule.as_view(), name='manager_approved'),
    path('manager_approved/<int:year>/<int:month>', ManagerApprovedAllSchedule.as_view(), name='manager_approved'),
    path('manager_application/', ManagerApplicationAllSchedule.as_view(), name='manager_application'),
    path(
        'manager_application/<int:year>/<int:month>/',
        ManagerApplicationAllSchedule.as_view(), name='manager_application'
    ),
    path('manager_schedule_regist/', ManagerScheduleRegistView.as_view(), name='manager_schedule_regist'),
    path('manager_schedule_detail/<int:pk>/', ManagerScheduleDetailView.as_view(), name='manager_schedule_detail'),
    path('manager_schedule_update/<int:pk>/', ManagerScheduleUpdateView.as_view(), name='manager_schedule_update'),
    path('manager_schedule_delete/<int:pk>/', ManagerScheduleDeleteView.as_view(), name='manager_schedule_delete'),

    # スタッフのURL
    path('staff_application_schedule/', StaffApplicationSchedule.as_view(), name='staff_application_schedule'),
    path('staff_approved_schedule/', StaffApprovedSchedule.as_view(), name='staff_approved_schedule'),
    path(
        'staff_application_schedule/<int:year>/<int:month>/',
        StaffApplicationSchedule.as_view(), name='staff_application_schedule'
    ),
    path(
        'staff_approved_schedule/<int:year>/<int:month>/',
        StaffApprovedSchedule.as_view(), name='staff_approved_schedule'
    ),
    path(
        'staff_schedule_day_regist/<int:year>/<int:month>/<int:day>',
        StaffScheduleDayRegistView.as_view(), name='staff_schedule_day_regist'
    ),
    path('staff_schedule_detail/<int:pk>/', StaffScheduleDetailView.as_view(), name='staff_schedule_detail'),
    path('staff_schedule_update/<int:pk>/', StaffScheduleUpdateView.as_view(), name='staff_schedule_update'),
    path('staff_schedule_delete/<int:pk>/', StaffScheduleDeleteView.as_view(), name='staff_schedule_delete'),
]
