# Generated by Django 4.2.4 on 2023-08-20 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_cv_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('fade', models.CharField(max_length=100)),
            ],
        ),
    ]