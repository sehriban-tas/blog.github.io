# Generated by Django 2.2.7 on 2019-11-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_post_field_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.ImageField(default='', upload_to='uploads/% Y/% m/% d/'),
        ),
    ]
