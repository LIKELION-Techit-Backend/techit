# Generated by Django 4.2.7 on 2023-12-23 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_taken'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='taken',
            unique_together={('member', 'lecture')},
        ),
    ]
