# Generated by Django 5.1.1 on 2024-09-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_feed_creation_time_alter_feed_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feed',
            options={'ordering': ('creation_time',)},
        ),
        migrations.AddField(
            model_name='feed',
            name='title',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='feed',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
