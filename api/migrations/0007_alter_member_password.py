# Generated by Django 4.2.7 on 2023-12-06 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_merge_0005_course_0005_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(default='your_default_value', max_length=20),
        ),
    ]
