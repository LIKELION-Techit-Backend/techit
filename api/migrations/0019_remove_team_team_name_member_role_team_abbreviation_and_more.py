# Generated by Django 4.2.7 on 2024-02-05 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_member_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pending',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('member', models.ForeignKey(db_column='member_id',
                 on_delete=django.db.models.deletion.CASCADE, related_name='pending_member', to='api.member')),
                ('team', models.ForeignKey(db_column='team_id',
                 on_delete=django.db.models.deletion.CASCADE, related_name='pending_team', to='api.team')),
            ],
        ),
    ]
