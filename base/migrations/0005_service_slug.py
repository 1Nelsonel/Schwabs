# Generated by Django 4.0.5 on 2023-04-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
