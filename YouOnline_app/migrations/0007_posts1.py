# Generated by Django 4.1.2 on 2022-10-28 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YouOnline_app', '0006_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='posts1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(db_index=True, editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('post', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
