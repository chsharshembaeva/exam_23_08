# Generated by Django 3.2 on 2022-08-23 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('month_to_learn', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('main_work', models.CharField(max_length=100)),
                ('experience', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=100)),
                ('work_study_place', models.CharField(blank=True, max_length=100, null=True)),
                ('has_own_notebook', models.BooleanField()),
                ('preferred_os', models.CharField(choices=[('windows', 'Windows'), ('macos', 'MacOS'), ('linux', 'Linux')], max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_started', models.DateField()),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.language')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.mentor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.student')),
            ],
        ),
    ]
