# Generated by Django 3.1.6 on 2021-03-29 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minute', '0006_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(default='', max_length=500),
        ),
    ]
