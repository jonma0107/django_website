# Generated by Django 3.2.25 on 2024-09-19 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-id']},
        ),
    ]
