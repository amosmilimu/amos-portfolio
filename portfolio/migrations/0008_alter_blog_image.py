# Generated by Django 4.2.4 on 2023-08-18 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='portfolio/media/img_bg_3.jpg', upload_to='portfolio/media/'),
        ),
    ]
