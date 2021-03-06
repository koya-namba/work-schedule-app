from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import (
    PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView,
    PasswordResetDoneView
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.views.generic.list import ListView

from .forms import (
    LoginForm, ManagerStaffRegistForm, ManagerStaffUpdateForm, StaffChangePasswordForm,
    SMPasswordResetForm, SMSetPasswordForm,
)
from .models import User
from article.models import Article


class IndexView(TemplateView):
    template_name = 'index.html'


class LogoutView(LoginRequiredMixin, View):
    """スタッフ・管理者共通のログアウトのView"""

    def get(self, requset, *args, **kwargs):
        logout(requset)
        return redirect('staff:index')


class ManagerMixin(UserPassesTestMixin):
    """管理者のみアクセス可能にするMixin"""

    def test_func(self):
        return self.request.user.is_staff


class ManagerHomeView(ManagerMixin, ListView):
    """管理者のホーム画面のView"""

    template_name = 'staff/manager_home.html'
    model = Article

    def get_queryset(self):
        qs = super(ManagerHomeView, self).get_queryset()
        qs = qs.order_by('-posted_at')
        return qs


class ManagerLoginView(FormView):
    """管理者のログイン画面のView"""

    template_name = 'staff/manager_login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        employee_id = request.POST['employee_id']
        password = request.POST['password']
        user = authenticate(employee_id=employee_id, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('staff:manager_home')
        else:
            messages.warning(request, 'IDかパスワードが異なります')
            return redirect('staff:manager_login')


class ManagerStaffDeleteView(ManagerMixin, DeleteView):
    """管理者がスタッフを削除するView"""

    model = User
    template_name = 'staff/manager_staff_delete.html'
    success_url = reverse_lazy('staff:manager_staff_list')


class ManagerStaffDetailView(ManagerMixin, DetailView):
    """管理者がスタッフの詳細をみるView"""

    model = User
    template_name = 'staff/manager_staff_detail.html'


class ManagerStaffListView(ManagerMixin, ListView):
    """管理者がスタッフの一覧をみるView"""

    model = User
    template_name = 'staff/manager_staff_list.html'

    def get_queryset(self):
        qs = super(ManagerStaffListView, self).get_queryset()
        qs = qs.order_by('employee_id')
        return qs


class ManagerStaffRegistView(ManagerMixin, CreateView):
    """管理者がスタッフを作成するView"""

    template_name = 'staff/manager_staff_regist.html'
    form_class = ManagerStaffRegistForm
    success_url = reverse_lazy('staff:manager_staff_list')

    def form_valid(self, form):
        return super().form_valid(form)


class ManagerStaffUpdateView(ManagerMixin, UpdateView):
    """管理者がスタッフを更新するView"""

    model = User
    template_name = 'staff/manager_staff_update.html'
    form_class = ManagerStaffUpdateForm

    def get_success_url(self):
        return reverse_lazy('staff:manager_staff_list')


class StaffChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    """スタッフがパスワードを変更するView"""

    form_class = StaffChangePasswordForm
    success_url = reverse_lazy('staff:staff_change_password_done')
    template_name = 'staff/staff_change_password.html'


class StaffChangePasswordDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    """パスワード更新後に遷移するView"""

    template_name = 'staff/staff_change_password_done.html'


class StaffHomeView(LoginRequiredMixin, ListView):
    """スタッフのホーム画面のView"""

    template_name = 'staff/staff_home.html'
    model = Article

    def get_queryset(self):
        qs = super(StaffHomeView, self).get_queryset()
        qs = qs.order_by('-posted_at')
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class StaffInformationView(LoginRequiredMixin, DetailView):
    """スタッフが自分の情報を確認するView"""

    template_name = 'staff/staff_information.html'

    def get(self, request, **kwargs):
        context = {'staff': self.request.user}
        return self.render_to_response(context)


class StaffLoginView(FormView):
    """スタッフがログインするView"""

    template_name = 'staff/staff_login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        employee_id = request.POST['employee_id']
        password = request.POST['password']
        user = authenticate(employee_id=employee_id, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('staff:staff_home')
        else:
            messages.warning(request, 'IDかパスワードが異なります')
            return redirect('staff:staff_login')


class SMPasswordResetView(PasswordResetView):
    """スタッフ・管理者がパスワードをリセットするのメールアドレス入力View"""

    template_name = 'staff/password_reset.html'
    form_class = SMPasswordResetForm
    from_email = 'namba.koya@arakawa-lab.com'
    success_url = reverse_lazy('password_reset_done')


class SMPasswordResetDoneView(PasswordResetDoneView):
    """スタッフ・管理者がパスワードリセットするためのメールを送信した後のView"""

    template_name = 'staff/password_reset_done.html'


class SMPasswordResetConfirmView(PasswordResetConfirmView):
    """スタッフ・管理者がパスワードをリセットするためのView"""

    template_name = 'staff/password_reset_confirmation.html'
    form_class = SMSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')


class SMPasswordResetCompleteView(PasswordResetCompleteView):
    """スタッフ・管理者がパスワードを更新した後のView"""

    template_name = 'staff/password_reset_complete.html'
