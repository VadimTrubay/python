# Generated by Django 4.2.3 on 2023-08-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("file_app", "0009_file_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="category",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="file",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]
