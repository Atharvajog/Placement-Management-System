# Generated by Django 4.1.3 on 2022-12-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_studentmodel_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
