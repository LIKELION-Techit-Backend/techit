from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):    
  id = models.BigAutoField(primary_key=True)
  first_name = models.CharField(max_length=20, null=False)
  last_name = models.CharField(max_length=20, null=False)
  email = models.CharField(max_length=30, null=False)
  password = models.CharField(max_length=20, null=False)
  
class Team(models.Model):
  id = models.BigAutoField(primary_key=True)
  team_name = models.CharField(max_length=30)

class Lecture(models.Model):
  id = models.BigAutoField(primary_key=True)
  lecture_name = models.CharField(max_length=100)
  course_id = models.ForeignKey('Course', related_name='course', on_delete=models.CASCADE, db_column="course_id")
  
class Course(models.Model):
  id = models.BigAutoField(primary_key=True)
  course_name = models.CharField(max_length=30)
  course_count = models.IntegerField(default=0)