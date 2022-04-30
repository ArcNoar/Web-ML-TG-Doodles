# Generated by Django 4.0.1 on 2022-04-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Prima_Word', '0004_alter_vm_word_word_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm_word',
            name='word_type',
            field=models.CharField(choices=[('VERB', 'Глагол'), ('ADJECTIVE', 'Прилагательное'), ('NOUN', 'Существительное'), ('STATE', 'Наречие'), ('NOMIN', 'Местоимение'), ('INTER', 'Междометие'), ('UNION', 'Союз'), ('PREPOS', 'Предлог'), ('NUMIN', 'Числительное'), ('PTICK', 'Частица'), ('PRICH', 'причастие'), ('DEPRICH', 'деепричастие'), ('PUNCTATION', 'Пунктуация'), ('NUM', 'Число'), ('SYMBOL', 'Символ'), ('NAME', 'Имя'), ('NONE_T', 'Не имеется')], default='NONE_T', max_length=20, verbose_name='Часть Речи'),
        ),
    ]
