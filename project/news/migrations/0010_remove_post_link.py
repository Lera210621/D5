# Generated by Django 4.1.3 on 2023-09-11 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_post_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='link',
        ),
    ]