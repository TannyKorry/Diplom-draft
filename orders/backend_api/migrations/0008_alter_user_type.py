# Generated by Django 3.2.22 on 2023-10-18 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('shop', 'Магазин'), ('Покупатель', 'buyer')], default='покупатель', max_length=10, verbose_name='Тип пользователя'),
        ),
    ]
