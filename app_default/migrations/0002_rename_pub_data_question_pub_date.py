# Generated by Django 4.0.2 on 2022-02-21 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_default', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
