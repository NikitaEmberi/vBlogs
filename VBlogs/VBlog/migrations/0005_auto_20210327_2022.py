# Generated by Django 3.1.7 on 2021-03-27 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VBlog', '0004_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
