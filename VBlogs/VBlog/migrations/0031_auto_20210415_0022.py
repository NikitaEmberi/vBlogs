# Generated by Django 3.1.7 on 2021-04-14 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VBlog', '0030_auto_20210415_0022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thoughts',
            old_name='user_id',
            new_name='user',
        ),
    ]