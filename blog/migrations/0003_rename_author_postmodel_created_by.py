# Generated by Django 5.0 on 2023-12-29 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_authormodel_first_name_authormodel_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='author',
            new_name='created_by',
        ),
    ]