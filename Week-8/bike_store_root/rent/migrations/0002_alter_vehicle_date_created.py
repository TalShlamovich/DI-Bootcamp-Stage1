# Generated by Django 4.1 on 2022-08-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
