# Generated by Django 3.1.5 on 2021-02-03 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210204_0157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='insta_url',
            new_name='instagram_url',
        ),
    ]