# Generated by Django 4.0.2 on 2022-10-28 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_movie_actors_alter_movie_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='db.Genre'),
        ),
    ]
