# Generated by Django 3.2.5 on 2021-07-26 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0003_auto_20210725_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentGrade',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='subject',
            name='classRoomName',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.RemoveField(
            model_name='student',
            name='studentSubjects',
        ),
        migrations.AddField(
            model_name='student',
            name='studentSubjects',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacherSubjects',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teacherSubjects',
            field=models.CharField(default='', max_length=30),
        ),
    ]
