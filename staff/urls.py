from django.urls import path

from .views import (
    IndexView, LogoutView,  ManagerLoginView, ManagerHomeView, ManagerStaffListView,
    ManagerStaffRegistView, ManagerStaffDetailView, ManagerStaffUpdateView, ManagerStaffDeleteView,
    StaffLoginView, StaffHomeView, StaffChangePasswordView, StaffChangePasswordDoneView,
    StaffInformationView,
)


app_name = 'staff'


urlpatterns = [
    # 管理者・スタッフ共通のURL
    path('', IndexView.as_view(), name='index'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # スタッフのURL
    path('staff_login', StaffLoginView.as_view(), name='staff_login'),
    path('staff_home/', StaffHomeView.as_view(), name='staff_home'),
    path('staff_information/', StaffInformationView.as_view(), name='staff_information'),
    path('staff_change_password/', StaffChangePasswordView.as_view(), name='staff_change_password'),
    path('staff_change_password_done/', StaffChangePasswordDoneView.as_view(), name='staff_change_password_done'),

    # 管理者のURL
    path('manager_login', ManagerLoginView.as_view(), name='manager_login'),
    path('manager_home/', ManagerHomeView.as_view(), name='manager_home'),
    path('manager_staff_list/', ManagerStaffListView.as_view(), name='manager_staff_list'),
    path('manager_staff_regist/', ManagerStaffRegistView.as_view(), name='manager_staff_regist'),
    path('manager_staff_detail/<int:pk>', ManagerStaffDetailView.as_view(), name='manager_staff_detail'),
    path('manager_staff_update/<int:pk>', ManagerStaffUpdateView.as_view(), name='manager_staff_update'),
    path('manager_staff_delete/<int:pk>', ManagerStaffDeleteView.as_view(), name='manager_staff_delete'),
]