# Generated by Django 4.1.3 on 2022-12-19 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_filesavingmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='roll_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]