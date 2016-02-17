# -*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

class Resume(models.Model):
    class Meta():
        db_table = 'resume'
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField()
    input_formats = ['%Y-%m-%d']

# --------------- My User Form--------------

class UserManager(BaseUserManager):
    def create_user(self, username, password, email=None):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email):
        user = self.create_user(username,
                                password=password,
                                email=email)
        user.is_admin = True
        user.save(using=self._db)
        return user

def get_upload_file_name(instance, filename):
        return '%s' % (filename)

class MyUser(AbstractBaseUser):
     username = models.CharField(verbose_name='Логин', max_length=150, unique=True)
     first_name = models.CharField(verbose_name='Имя', max_length=30, blank=False)
     last_name = models.CharField(verbose_name='Фамилия', max_length=30, blank=False)
     email = models.EmailField(verbose_name='Электронная почта', max_length=255, unique=True)
     b_day = models.DateField(verbose_name='Дата рождения', blank=False, null=False)
     phone = models.CharField(verbose_name='Телефон', max_length=15, unique=True)
     avatar = models.FileField(verbose_name='Аватар', upload_to=get_upload_file_name, blank=True, null=True)
     is_active = models.BooleanField('Активен', default=True)
     is_admin = models.BooleanField('Админ', default=False)

     objects = UserManager()

     USERNAME_FIELD = 'username'
     REQUIRED_FIELDS = ['email']



     def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name,)

     def get_short_name(self):
        last = self.last_name[0]                    # вывод полного имени в формате "Евгений М."
        return '%s %s' % (self.first_name, last,)

     def __str__(self):
        return self.username

     def has_perm(self, perm, obj=None):
        return True

     def has_module_perms(self, app_label):
        return True

     @property
     def is_staff(self):
        return self.is_admin
