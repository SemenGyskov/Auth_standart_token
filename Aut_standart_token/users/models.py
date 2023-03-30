from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,PermissionsMixin, BaseUserManager

class MyUserManager(BaseUserManager):
    def _create_user(self, email,username, password, **extra_fields):
        if not email:
            raise ValueError('Вы не указали email')
        if not username:
            raise ValueError('Вы не указали Логин')
        user = self.model(email=self.normalize_email(email), username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, username, password):
        return self._create_user(email, username, password)
    def create_superuser(self, email, username, password):
        return self._create_superuser(email, username, password, id_staff=True, id_superuser=True)

class User(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyUserManager()

    def __str__(self):
        return self.email

