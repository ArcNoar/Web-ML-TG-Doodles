# Generated by Django 4.0.1 on 2022-03-18 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asiya', '0004_rename_mult_vm_word_mult'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm_word',
            name='proper_noun',
            field=models.BooleanField(default=False, verbose_name='Имя собственное ?'),
        ),
    ]
