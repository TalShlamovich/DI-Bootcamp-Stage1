# Generated by Django 4.1 on 2022-08-14 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_director_film_available_in_film_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='created_in',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='films.country'),
        ),
    ]
