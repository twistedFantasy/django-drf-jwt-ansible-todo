from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from taggit.managers import TaggableManager

from todo.core.models import BaseModel


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, BaseModel):
    email = models.EmailField('Email', unique=True, max_length=256)
    full_name = models.CharField('Full Name', max_length=256, default='', blank=True)
    date_of_birth = models.DateField('Date Of Birth', null=True, blank=True)
    is_active = models.BooleanField('Is Active', default=True)
    is_staff = models.BooleanField('Is Staff', default=False, db_index=True)
    is_superuser = models.BooleanField('Is Superuser', default=False, db_index=True)

    tags = TaggableManager('Tags', blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        app_label = 'users'
        verbose_name_plural = 'Users'
        ordering = ['-modified']

    def __str__(self):
        return f'{self.get_full_name()} (user {self.id})'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def has_tag(obj, tag):
        return tag in obj.tags.names()
