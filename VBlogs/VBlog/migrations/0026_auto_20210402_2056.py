# Generated by Django 3.1.7 on 2021-04-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VBlog', '0025_categories_meta_titles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='Meta_Titles',
            field=models.CharField(max_length=255),
        ),
    ]
