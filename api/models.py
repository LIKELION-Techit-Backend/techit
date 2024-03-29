from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Member(AbstractUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = None  # username을 사용 안할 경우
    email = models.EmailField(('email'), unique=True)
    team = models.ForeignKey(
        'Team', related_name='team', on_delete=models.CASCADE, db_column="team_id", null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Pending(models.Model):
    id = models.BigAutoField(primary_key=True)
    member = models.ForeignKey(
        'Member', related_name='pending_member', on_delete=models.CASCADE, db_column="member_id")
    team = models.ForeignKey(
        'Team', related_name='pending_team', on_delete=models.CASCADE, db_column="team_id")


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    abbreviation = models.CharField(max_length=10, unique=True, blank=True)
    name = models.CharField(max_length=30, unique=True, blank=True)


class Lecture(models.Model):
    id = models.BigAutoField(primary_key=True)
    lecture_name = models.CharField(max_length=100)
    course_id = models.ForeignKey(
        'Course', related_name='course', on_delete=models.CASCADE, db_column="course_id")


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=64, unique=True)


class Taken(models.Model):
    id = models.BigAutoField(primary_key=True)
    member = models.ForeignKey(
        'Member', related_name='member', on_delete=models.CASCADE, db_column="member_id")
    lecture = models.ForeignKey(
        'Lecture', related_name='lecture', on_delete=models.CASCADE, db_column="lecture_id")

    class Meta:
        unique_together = ['member', 'lecture']
