# Generated by Django 3.1.13 on 2021-09-24 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_revise_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='authors',
            new_name='author',
        ),
    ]