# Generated by Django 5.0.6 on 2024-06-23 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_postcomment_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='image_user',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='name_button',
        ),
    ]