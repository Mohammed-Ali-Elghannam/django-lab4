# Generated by Django 5.1.7 on 2025-03-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.IntegerField(help_text='Duration in Hours'),
        ),
    ]
