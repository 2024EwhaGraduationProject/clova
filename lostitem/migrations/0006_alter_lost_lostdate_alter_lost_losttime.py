# Generated by Django 4.2.7 on 2024-09-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lostitem', '0005_lost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='lostdate',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lost',
            name='losttime',
            field=models.TextField(blank=True, null=True),
        ),
    ]