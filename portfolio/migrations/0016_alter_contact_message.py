# Generated by Django 4.2.4 on 2023-08-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_yearsofexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=250),
        ),
    ]