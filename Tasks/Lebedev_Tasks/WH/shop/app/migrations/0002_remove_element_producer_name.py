# Generated by Django 3.2.3 on 2021-06-10 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='element',
            name='Producer_Name',
        ),
    ]