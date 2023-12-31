# Generated by Django 4.1.7 on 2023-03-27 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_my_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='quotes', to='app_my_site.author'),
        ),
        migrations.RemoveField(
            model_name='quote',
            name='tags',
        ),
        migrations.AddField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(related_name='quotes', to='app_my_site.tag'),
        ),
    ]
