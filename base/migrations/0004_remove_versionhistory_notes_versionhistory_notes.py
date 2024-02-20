# Generated by Django 5.0.2 on 2024-02-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_versionhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='versionhistory',
            name='notes',
        ),
        migrations.AddField(
            model_name='versionhistory',
            name='notes',
            field=models.JSONField(default={}),
        ),
    ]
