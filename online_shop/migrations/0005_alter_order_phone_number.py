# Generated by Django 5.0.7 on 2024-08-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0004_alter_comment_is_provide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]
