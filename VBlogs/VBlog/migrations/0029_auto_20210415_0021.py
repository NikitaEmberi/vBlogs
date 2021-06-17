# Generated by Django 3.1.7 on 2021-04-14 18:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('VBlog', '0028_trendingemailnotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thoughts',
            name='email',
        ),
        migrations.RemoveField(
            model_name='thoughts',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='thoughts',
            name='last_name',
        ),
        migrations.AddField(
            model_name='thoughts',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]