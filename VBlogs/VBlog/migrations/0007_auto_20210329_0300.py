# Generated by Django 3.1.7 on 2021-03-28 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VBlog', '0006_post_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Categories',
            field=models.CharField(default="['uncategorised']", max_length=255),
        ),
    ]