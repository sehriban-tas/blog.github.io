# Generated by Django 2.2.7 on 2019-11-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='field_name',
            field=models.ImageField(default='', upload_to=None),
        ),
    ]
