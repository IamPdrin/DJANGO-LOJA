# Generated by Django 5.0.6 on 2024-05-28 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appHome', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='sobrenome',
            new_name='email',
        ),
    ]
