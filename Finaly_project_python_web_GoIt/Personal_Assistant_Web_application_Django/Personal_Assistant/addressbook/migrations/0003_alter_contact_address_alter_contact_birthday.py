# Generated by Django 4.2.3 on 2023-07-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addressbook", "0002_alter_contact_address_alter_contact_birthday_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="address",
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="contact",
            name="birthday",
            field=models.DateField(null=True),
        ),
    ]
