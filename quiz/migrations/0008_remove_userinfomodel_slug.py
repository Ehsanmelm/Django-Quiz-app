# Generated by Django 4.0.6 on 2022-09-30 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_alter_userinfomodel_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfomodel',
            name='slug',
        ),
    ]
