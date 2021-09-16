from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse_lazy


class UserManager(BaseUserManager):
    """ユーザ作成をカスタマイズ
    employee_id: ユニーク
    """

    def create_user(self, employee_id, password=None):
        """アクティブユーザの作成"""
        if not employee_id:
            raise ValueError('Enter employee_id')
        user = self.model(employee_id=employee_id,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, employee_id, password=None):
        """スーパーユーザの作成"""
        user = self.model(employee_id=employee_id)
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """ユーザ(スタッフ)のモデル"""

    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    tel_number = models.CharField(validators=[MinLengthValidator(9)], max_length=11, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    zipcode = models.CharField(validators=[MinLengthValidator(7)], max_length=7, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'employee_id'
    REQUIRED_FIELD = []

    objects = UserManager()

    def __str__(self):
        return self.employee_id

    def get_absolute_url(self):
        return reverse_lazy('staff:staff_home')
