# Generated by Django 3.2.22 on 2023-10-18 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0009_alter_user_type'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='orderitem',
            name='unique_order_item',
        ),
    ]
