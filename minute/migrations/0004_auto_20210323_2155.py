# Generated by Django 3.1.6 on 2021-03-23 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minute', '0003_auto_20210323_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberspresent',
            name='flyminute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberspresent_set', to='minute.fly_minute'),
        ),
    ]