# Generated by Django 4.0.1 on 2022-03-17 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asiya', '0002_alter_vm_word_word_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='vm_word',
            name='Mult',
            field=models.BooleanField(default=False, verbose_name='Слово - Множественное'),
        ),
        migrations.AddField(
            model_name='vm_word',
            name='word_case',
            field=models.CharField(choices=[('IMP', 'Именительный'), ('RP', 'Родительный'), ('DP', 'Дательный'), ('VP', 'Винительный'), ('TP', 'Творительный'), ('PP', 'Предложный'), ('None', 'Без падежа')], default='None', max_length=16, verbose_name='Падеж'),
        ),
    ]