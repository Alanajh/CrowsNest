# Generated by Django 4.2.13 on 2024-06-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('columns', models.CharField(max_length=10)),
                ('rows', models.CharField(max_length=10)),
            ],
        ),
    ]