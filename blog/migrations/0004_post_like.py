# Generated by Django 2.1.11 on 2020-12-23 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201223_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(null=True),
        ),
    ]
