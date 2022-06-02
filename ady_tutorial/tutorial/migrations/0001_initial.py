# Generated by Django 3.2.12 on 2022-04-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=100)),
                ('stu_class', models.CharField(max_length=20)),
                ('stu_branch', models.CharField(max_length=100)),
                ('collage_name', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
        ),
    ]