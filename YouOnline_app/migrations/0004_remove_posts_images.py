# Generated by Django 4.1.2 on 2022-10-28 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('YouOnline_app', '0003_delete_article_posts_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='images',
        ),
    ]
