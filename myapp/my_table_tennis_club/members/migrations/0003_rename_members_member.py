# Generated by Django 3.2.5 on 2023-06-09 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20230608_2240'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='members',
            new_name='Member',
        ),
    ]