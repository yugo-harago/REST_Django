# Generated by Django 4.1 on 2022-10-07 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="description",
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
