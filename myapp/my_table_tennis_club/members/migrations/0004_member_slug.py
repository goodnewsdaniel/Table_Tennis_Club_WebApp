# Generated by Django 3.2.5 on 2024-01-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_members_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
