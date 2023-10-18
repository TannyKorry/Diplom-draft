# Generated by Django 3.2.22 on 2023-10-18 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0012_alter_productparameter_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Заказанная позиция', 'verbose_name_plural': 'Список заказанных позиций'},
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(verbose_name='Время создания'),
        ),
    ]
