# Generated by Django 4.2.4 on 2023-08-18 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_blog_category_blog_datecreated_blog_views_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='portfolio/static/portfolio/img_bg_3.jpg', upload_to='portfolio/static/portfolio/images'),
        ),
    ]
