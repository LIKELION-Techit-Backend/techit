# Generated by Django 4.2.7 on 2023-12-16 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_lecture_course_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='course_id',
            field=models.ForeignKey(db_column='course_id', on_delete=django.db.models.deletion.CASCADE, related_name='course', to='api.course'),
        ),
    ]
