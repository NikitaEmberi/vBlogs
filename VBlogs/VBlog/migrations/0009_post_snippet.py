# Generated by Django 3.1.7 on 2021-03-29 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VBlog', '0008_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the button below to read the post.', max_length=255),
        ),
    ]
