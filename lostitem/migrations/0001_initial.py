# Generated by Django 5.1 on 2024-08-10 15:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('informations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('lostdate', models.DateField()),
                ('losttime', models.TimeField()),
                ('description', models.CharField(blank=True, null=True, max_length=255)),
                ('moredesc', models.CharField(blank=True, null=True, max_length=255)),
                ('finished', models.BooleanField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemcategory', to='informations.category')),
                ('getwhere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemgetwhere', to='informations.location')),
                ('nowwhere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemnowwhere', to='informations.location')),
                ('userget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemuserget', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
