from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


User = get_user_model()


class LoginForm(forms.Form):
    """管理者，スタッフ共通のログインフォーム"""

    employee_id = forms.CharField(label='ID')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())


class ManagerStaffRegistForm(forms.ModelForm):
    """管理者がスタッフを作成するフォーム"""

    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='password再入力', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('employee_id', 'name', 'birthday', 'email', 'tel_number', 'zipcode', 'password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません')

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data.get("password"))
        user.save()
        return user


class ManagerStaffUpdateForm(forms.ModelForm):
    """管理者がスタッフ情報を更新するフォーム"""

    class Meta:
        model = User
        fields = ('name', 'birthday', 'email', 'tel_number', 'zipcode',)

    def save(self, commit=False):
        user = super().save(commit=False)
        user.save()
        return user


class StaffChangePasswordForm(PasswordChangeForm):
    """スタッフがパスワードを変更するフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SMPasswordResetForm(PasswordResetForm):
    """スタッフ・管理者がパスワードをリセットするためのメールアドレスを入力するForm"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SMSetPasswordForm(SetPasswordForm):
    """スタッフ・管理者がパスワードを変更するためのForm"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
