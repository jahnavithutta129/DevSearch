# Generated by Django 5.0.4 on 2024-04-08 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_message_body_alter_message_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
