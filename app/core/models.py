from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extraFields):
        if not email:
            raise ValueError("Only valid email addresses are expected.")
        user = self.model(email=self.normalize_email(email), **extraFields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,password):
        user = self.model(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser= True
        user.save(using=self._db)

        return user



class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"