# Generated by Django 5.1.1 on 2024-10-15 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_writeup_wid_writeup_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writeup',
            name='author',
        ),
        migrations.RemoveField(
            model_name='writeup',
            name='id',
        ),
        migrations.AlterField(
            model_name='writeup',
            name='title',
            field=models.CharField(default='', max_length=64, primary_key=True, serialize=False),
        ),
    ]
