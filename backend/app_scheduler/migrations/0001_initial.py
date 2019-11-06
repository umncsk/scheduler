# Generated by Django 2.2.5 on 2019-11-06 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('team_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('team_schedule', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=256)),
                ('user_pswd', models.CharField(max_length=256)),
                ('student_id', models.CharField(max_length=20)),
                ('student_pswd', models.CharField(max_length=256)),
                ('user_schedule', models.CharField(max_length=256)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_scheduler.Organization')),
            ],
        ),
    ]
