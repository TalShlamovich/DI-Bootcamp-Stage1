# Generated by Django 4.1 on 2022-08-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='available_in',
            field=models.ManyToManyField(blank=True, related_name='films', to='films.country'),
        ),
        migrations.AddField(
            model_name='film',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='films', to='films.category'),
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.ManyToManyField(blank=True, related_name='films', to='films.director'),
        ),
    ]