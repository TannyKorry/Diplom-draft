# Generated by Django 3.2.22 on 2023-10-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0012_auto_20231019_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]