# Generated by Django 5.1.1 on 2024-10-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_writeup_content_writeup_page_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='writeup',
            name='wid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='writeup',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
    ]
