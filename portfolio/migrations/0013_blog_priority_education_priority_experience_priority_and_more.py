# Generated by Django 4.2.4 on 2023-08-20 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_generalskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experience',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generalskill',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skill',
            name='priority',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
