# Generated by Django 4.1.2 on 2023-05-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=20)),
                ('EmailId', models.EmailField(max_length=254)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('UserName', models.CharField(max_length=10)),
                ('Address', models.TextField()),
                ('Profession', models.CharField(max_length=20)),
                ('Courses', models.CharField(max_length=20)),
                ('EmailId', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'register',
            },
        ),
    ]