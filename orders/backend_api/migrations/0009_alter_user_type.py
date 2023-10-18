# Generated by Django 3.2.22 on 2023-10-18 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0008_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('shop', 'Магазин'), ('buyer', 'Покупатель')], default='покупатель', max_length=10, verbose_name='Тип пользователя'),
        ),
    ]
