# Generated by Django 4.0.1 on 2022-03-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asiya', '0011_vm_word_w_face'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm_word',
            name='w_declin',
            field=models.CharField(choices=[('INDIC', 'Индикатив'), ('SUBINDIC', 'Субьюнктив'), ('IMPER', 'Императив'), ('None', 'Нет Наклонения')], default='None', max_length=16, verbose_name='Склонение'),
        ),
    ]
