# Generated by Django 3.0.7 on 2020-06-15 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebuddy', '0005_auto_20200615_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_url',
            field=models.URLField(),
        ),
    ]