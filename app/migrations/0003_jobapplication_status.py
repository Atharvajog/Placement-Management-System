# Generated by Django 4.1.3 on 2022-12-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('Applied', 'Applied'), ('Placed', 'Placed'), ('Rejected', 'Rejected')], default=('Applied', 'Applied'), max_length=10),
        ),
    ]
