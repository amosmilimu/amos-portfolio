# Generated by Django 4.2.4 on 2023-08-22 11:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_education_collapse_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
