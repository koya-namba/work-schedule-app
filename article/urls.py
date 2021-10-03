from django.urls import path
from .views import (
    ManagerCreateArticleView, ManagerDeleteArticleView, ManagerUpdateArticleView,
    StaffCreateArticleView, StaffDeleteArticleView, StaffUpdateArticleView
)

app_name = 'article'

urlpatterns = [
    path('manager_create_article/', ManagerCreateArticleView.as_view(), name='manager_create_article'),
    path('manager_delete_article/<int:pk>/', ManagerDeleteArticleView.as_view(), name='manager_delete_article'),
    path('manager_update_article/<int:pk>/', ManagerUpdateArticleView.as_view(), name='manager_update_article'),
    path('staff_create_article/', StaffCreateArticleView.as_view(), name='staff_create_article'),
    path('staff_delete_article/<int:pk>/', StaffDeleteArticleView.as_view(), name='staff_delete_article'),
    path('staff_update_article/<int:pk>/', StaffUpdateArticleView.as_view(), name='staff_update_article'),
]
