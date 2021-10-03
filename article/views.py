from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import (
    ManagerCreateArticleForm, ManagerUpdateArticleForm, StaffCreateArticleForm, StaffUpdateArticleForm
)
from .models import Article
from staff.views import ManagerMixin


class ManagerCreateArticleView(ManagerMixin, CreateView):
    """管理者が記事を作成するView"""

    model = Article
    template_name = 'article/manager_create_article.html'
    form_class = ManagerCreateArticleForm
    success_url = reverse_lazy('staff:manager_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ManagerCreateArticleView, self).form_valid(form)


class ManagerDeleteArticleView(ManagerMixin, DeleteView):
    """管理者が記事を削除するView"""

    model = Article
    template_name = 'article/manager_delete_article.html'
    success_url = reverse_lazy('staff:manager_home')


class ManagerUpdateArticleView(ManagerMixin, UpdateView):
    """管理者がスケジュールを更新するView"""

    model = Article
    template_name = 'article/manager_update_article.html'
    form_class = ManagerUpdateArticleForm

    def get_success_url(self):
        return reverse_lazy('staff:manager_home')


class StaffCreateArticleView(LoginRequiredMixin, CreateView):
    """スタッフが記事を作成するView"""

    model = Article
    template_name = 'article/staff_create_article.html'
    form_class = StaffCreateArticleForm
    success_url = reverse_lazy('staff:staff_home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(StaffCreateArticleView, self).form_valid(form)


class StaffDeleteArticleView(LoginRequiredMixin, DeleteView):
    """スタッフが記事を削除するView"""

    model = Article
    template_name = 'article/staff_delete_article.html'
    success_url = reverse_lazy('staff:staff_home')


class StaffUpdateArticleView(LoginRequiredMixin, UpdateView):
    """スタッフがスケジュールを更新するView"""

    model = Article
    template_name = 'article/staff_update_article.html'
    form_class = StaffUpdateArticleForm

    def get_success_url(self):
        return reverse_lazy('staff:staff_home')
