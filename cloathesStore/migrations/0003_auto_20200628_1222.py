# Generated by Django 2.2.13 on 2020-06-28 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloathesStore', '0002_auto_20200627_0831'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userquestion',
            old_name='adminEmail',
            new_name='email',
        ),
    ]
