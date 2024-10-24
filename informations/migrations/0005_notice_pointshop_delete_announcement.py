# Generated by Django 5.1 on 2024-08-17 10:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0004_announcement_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, null=True, max_length=255)),
                ('noticeDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('contents', models.CharField(blank=True, null=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PointShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuff', models.CharField(blank=True, null=True, max_length=255)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('soldout', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Announcement',
        ),
    ]
