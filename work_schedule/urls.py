from django.contrib import admin
from django.urls import path, include

from staff.views import (
    SMPasswordResetView, SMPasswordResetDoneView, SMPasswordResetConfirmView, SMPasswordResetCompleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staff.urls')),
    path('schedule/', include('schedule.urls')),
    path('article/', include('article.urls')),

    # パスワードをリセットするためのURL
    path('password_reset/', SMPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', SMPasswordResetDoneView.as_view(), name='password_reset_done'),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        SMPasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    path(
        'password_reset_complete/',
        SMPasswordResetCompleteView.as_view(), name='password_reset_complete'
    ),
]
