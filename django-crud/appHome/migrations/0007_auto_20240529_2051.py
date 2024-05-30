# Generated by Django 5.0.6 on 2024-05-29 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHome', '0006_rename_produto_usuario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Produto',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='sobrenome',
            new_name='preco',
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
