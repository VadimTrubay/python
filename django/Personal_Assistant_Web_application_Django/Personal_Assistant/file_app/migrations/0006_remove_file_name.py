# Generated by Django 4.2.3 on 2023-07-25 09:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("file_app", "0005_alter_file_file"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="file",
            name="name",
        ),
    ]
