# Generated by Django 5.1.1 on 2024-09-27 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_feed_options_feed_title_alter_feed_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feed',
            options={'ordering': ('-creation_time',)},
        ),
    ]
