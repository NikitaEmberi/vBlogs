# Generated by Django 3.1.7 on 2021-04-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VBlog', '0020_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]