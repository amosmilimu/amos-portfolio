# Generated by Django 4.2.4 on 2023-08-19 15:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]