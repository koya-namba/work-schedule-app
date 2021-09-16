from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import ManagerStaffUpdateForm, ManagerStaffRegistForm


User = get_user_model()


class CustomizeUserAdmin(UserAdmin):
    """adminユーザのインタフェースのカスタマイズ"""

    form = ManagerStaffUpdateForm
    add_form = ManagerStaffRegistForm
    list_display = ('employee_id', 'name', 'tel_number')
    ordering = ('employee_id',)
    search_fields = ('name',)
    fieldsets = (
        ('ユーザ情報', {
            'fields': ('employee_id', 'password', 'name', 'birthday', 'email', 'tel_number', 'zipcode',)
        }),
        ('パーミッション', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        ('ユーザ情報', {
            'fields': (
                'employee_id', 'name', 'birthday', 'email',
                'tel_number', 'zipcode', 'password', 'confirm_password'
            )
        }),
    )


admin.site.register(User, CustomizeUserAdmin)
