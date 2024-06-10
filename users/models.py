# # from django.db import models
# # from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# # from django.contrib.auth.models import User
# # from django.utils import timezone
# # from django.utils.translation import gettext_lazy as _
# # from django.contrib.auth.models import Group, Permission
# # from django.db.models import CASCADE    
# # from django.contrib.auth.models import AbstractUser, Group, Permission




# # class CustomUserManager(BaseUserManager):
# #     def create_user(self, email, password=None, **extra_fields):
# #         if not email:
# #             raise ValueError('The Email field must be set')
# #         email = self.normalize_email(email)
# #         user = self.model(email=email, **extra_fields)
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user

# #     def create_superuser(self, email, password=None, **extra_fields):
# #         extra_fields.setdefault('is_staff', True)
# #         extra_fields.setdefault('is_superuser', True)

# #         if extra_fields.get('is_staff') is not True:
# #             raise ValueError('Superuser must have is_staff=True.')
# #         if extra_fields.get('is_superuser') is not True:
# #             raise ValueError('Superuser must have is_superuser=True.')

# #         return self.create_user(email, password, **extra_fields)

# # class CustomUser(AbstractBaseUser, PermissionsMixin):
# #     email = models.EmailField(unique=True)
# #     username = models.CharField(max_length=150, blank=True, null=True)
# #     is_active = models.BooleanField(default=True)
# #     is_staff = models.BooleanField(default=False)
# #     date_joined = models.DateTimeField(auto_now_add=True)

# #     objects = CustomUserManager()

# #     USERNAME_FIELD = 'email'
# #     REQUIRED_FIELDS = []

# #     def __str__(self):
# #         return self.email
    
    
    
# #     class Meta:
# #         verbose_name = 'User'
# #         verbose_name_plural = 'Users'
        

# # Group.add_to_class('custom_user_set', models.ManyToManyField(CustomUser, through='GroupUser', through_fields=('group', 'user')))
# # Permission.add_to_class('custom_user_set', models.ManyToManyField(CustomUser, through='UserPermission', through_fields=('permission', 'user')))
    
    
    


# # # class CustomUser(AbstractUser):
# # #     # Add your custom fields here
    
# # #     class Meta:
# # #         verbose_name = 'User'
# # #         verbose_name_plural = 'Users'

# #     # class Meta:
# #     #     unique_together = ['user', 'group']

# # # class UserPermission(models.Model):
# # #     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
# # #     permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

# # #     class Meta:
# # #         unique_together = ['user', 'permission']

    
# # # CustomUser._meta.get_field('groups').remote_field.related_query_name = 'customuser_groups'
# # # CustomUser._meta.get_field('user_permissions').remote_field.related_query_name = 'customuser_user_permissions'


# # class UserProfile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     email_confirmed = models.BooleanField(default=False)
# #     first_name = models.CharField(_('first name'), max_length=30, blank=True)
# #     last_name = models.CharField(_('last name'), max_length=150, blank=True)
# #     date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
# #     location = models.CharField(_('location'), max_length=100, blank=True)
# #     bio = models.TextField(_('bio'), max_length=500, blank=True)

# #     def __str__(self):
# #         return self.user.username


# # class EmailVerificationToken(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)
# #     token = models.CharField(_('token'), max_length=100)
# #     created_at = models.DateTimeField(_('created at'), default=timezone.now)
# #     expiration_date = models.DateTimeField(_('expiration date'), null=True)

# #     def __str__(self):
# #         return self.user.username + ' - ' + self.token





# '----------------------------------------------------------------'

# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
# from django.utils.translation import gettext_lazy as _
# from django.utils import timezone





# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)


# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'


# class GroupUser(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ['user', 'group']


# class UserPermission(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ['user', 'permission']


# # Define the many-to-many relationships with custom through models
# CustomUser.groups.through = GroupUser
# CustomUser.user_permissions.through = UserPermission

  








# class UserProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     email_confirmed = models.BooleanField(default=False)
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=150, blank=True)
#     date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
#     location = models.CharField(_('location'), max_length=100, blank=True)
#     bio = models.TextField(_('bio'), max_length=500, blank=True)

#     def __str__(self):
#         return self.user.username


# class EmailVerificationToken(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     token = models.CharField(_('token'), max_length=100)
#     created_at = models.DateTimeField(_('created at'), default=timezone.now)
#     expiration_date = models.DateTimeField(_('expiration date'), null=True)

#     def __str__(self):
#         return self.user.username + ' - ' + self.token



"'''''''''''''''''''''''''''''''''''''''CoinHub/'"


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)




class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Add custom related names for many-to-many relationships
    groups = models.ManyToManyField(Group, through='GroupUser', related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, through='UserPermission', related_name='custom_users')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'







# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=150, blank=True, null=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'


class GroupUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'group']


class UserPermission(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'permission']


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)
    location = models.CharField(_('location'), max_length=100, blank=True)
    bio = models.TextField(_('bio'), max_length=500, blank=True)

    def __str__(self):
        return self.user.username


class EmailVerificationToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    token = models.CharField(_('token'), max_length=100)
    created_at = models.DateTimeField(_('created at'), default=timezone.now)
    expiration_date = models.DateTimeField(_('expiration date'), null=True)

    def __str__(self):
        return f"{self.user.username} - {self.token}"
