# Generated by Django 2.2 on 2020-12-16 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church_app', '0007_auto_20201209_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='church',
            name='twitter',
        ),
    ]
