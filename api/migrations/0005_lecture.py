# Generated by Django 4.2.7 on 2023-12-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_member_email_member_password_alter_member_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('lecture_name', models.CharField(max_length=100)),
                ('course_id', models.CharField(max_length=20)),
            ],
        ),
    ]