# Generated by Django 5.0.7 on 2024-08-01 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0003_comment_is_provide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='is_provide',
            field=models.BooleanField(default=True),
        ),
    ]
