# Generated by Django 3.1.4 on 2020-12-31 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20201228_1916'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ('-subscribed_date',), 'verbose_name_plural': 'Users'},
        ),
    ]
