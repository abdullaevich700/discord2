# Generated by Django 4.2.4 on 2023-08-08 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_topicmodel_roommodel_host_messagemodel_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roommodel',
            options={'ordering': ('-created', '-updated')},
        ),
    ]