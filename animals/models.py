from django.db import models

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class Post(models.Model):

    PUBLISH = 0
    NOT_PUBLISH = 1

    STATUS = (
        (PUBLISH, "Publish"),
        (NOT_PUBLISH, "Not Publish"),
    )

    # post_id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Title", max_length=200)
    content = models.TextField(
        max_length=2000, help_text="Enter you blog text here.")
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    status = models.IntegerField(
        verbose_name="Status", choices=STATUS, default=0)
    created_by = models.CharField(verbose_name="Created By", max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    commented_by = models.CharField(verbose_name="Created By", max_length=200)
    comment = models.TextField(max_length=2000, help_text="Comments..")
    post = models.CharField(verbose_name="Post Ref", max_length=200)
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.post


# Acount Modify

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     date_joined = models.DateTimeField(
#         verbose_name='date joined', auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email

#     # For checking permissions. to keep it simple all admin have ALL permissons
#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
#     def has_module_perms(self, app_label):
#         return True
