# Generated by Django 4.1.3 on 2023-08-05 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_author_comment_post_postcategory_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('new', 'Новость'), ('article', 'Статья')], default='new', max_length=20),
        ),
    ]