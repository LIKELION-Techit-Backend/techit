# Generated by Django 4.2.7 on 2023-12-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_member_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]