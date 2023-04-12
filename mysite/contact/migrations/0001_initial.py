# Generated by Django 4.1.6 on 2023-03-26 05:51

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
    ]