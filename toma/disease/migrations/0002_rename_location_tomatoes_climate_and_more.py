# Generated by Django 4.2.5 on 2023-09-14 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tomatoes',
            old_name='location',
            new_name='climate',
        ),
        migrations.RenameField(
            model_name='tomatoes',
            old_name='desc',
            new_name='diagnosis',
        ),
    ]