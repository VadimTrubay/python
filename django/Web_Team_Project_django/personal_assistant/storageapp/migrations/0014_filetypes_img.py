# Generated by Django 4.2.1 on 2023-05-17 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("storageapp", "0013_remove_file_file_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="filetypes",
            name="img",
            field=models.ImageField(default="icons/other.jpeg", upload_to=""),
        ),
    ]