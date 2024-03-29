# Generated by Django 3.2.18 on 2023-04-14 23:58

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
                ('contact_name', models.CharField(max_length=70)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_subject', models.TextField()),
                ('contact_message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='latestNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=300)),
                ('userName', models.CharField(max_length=50)),
                ('userProfile', models.CharField(max_length=100)),
                ('views', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('desc', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('image', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('mail_id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='trendingNews',
            fields=[
                ('category', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('image', models.CharField(max_length=300)),
            ],
        ),
    ]
