# Generated by Django 5.0.6 on 2024-06-22 08:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=25, unique=True)),
                ('born_date', models.DateTimeField()),
                ('born_location', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=500)),
                ('tags', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quoteapp.author')),
            ],
        ),
    ]
