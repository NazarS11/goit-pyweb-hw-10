# Generated by Django 5.0.6 on 2024-06-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0006_alter_author_born_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(max_length=100),
        ),
    ]
