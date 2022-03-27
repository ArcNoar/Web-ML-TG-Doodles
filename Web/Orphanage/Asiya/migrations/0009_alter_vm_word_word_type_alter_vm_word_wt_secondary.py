# Generated by Django 4.0.1 on 2022-03-21 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asiya', '0008_remove_vm_word_mult_vm_word_antonym_w_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vm_word',
            name='word_type',
            field=models.CharField(choices=[('VERB', 'Глагол'), ('ADJECTIVE', 'Прилагательное'), ('NOUN', 'Существительное'), ('STATE', 'Наречие'), ('NOMIN', 'Местоимение'), ('INTER', 'Междометие'), ('PRICH', 'Причастие'), ('DEPRICH', 'Деепричастие'), ('UNION', 'Союз'), ('PREPOS', 'Предлог'), ('NUMIN', 'Числительное'), ('PREDICAT', 'Предикатив'), ('PUNCTATION', 'Пунктуация'), ('NUM', 'Число'), ('SYMBOL', 'Символ'), ('SMILE', 'Смайл'), ('NONE_T', 'Не имеется')], default='NOUN', max_length=20, verbose_name='Часть Речи'),
        ),
        migrations.AlterField(
            model_name='vm_word',
            name='wt_secondary',
            field=models.CharField(choices=[('VERB', 'Глагол'), ('ADJECTIVE', 'Прилагательное'), ('NOUN', 'Существительное'), ('STATE', 'Наречие'), ('NOMIN', 'Местоимение'), ('INTER', 'Междометие'), ('PRICH', 'Причастие'), ('DEPRICH', 'Деепричастие'), ('UNION', 'Союз'), ('PREPOS', 'Предлог'), ('NUMIN', 'Числительное'), ('PREDICAT', 'Предикатив'), ('PUNCTATION', 'Пунктуация'), ('NUM', 'Число'), ('SYMBOL', 'Символ'), ('SMILE', 'Смайл'), ('NONE_T', 'Не имеется')], default='NONE_T', max_length=20, verbose_name='Адаптивная часть речи'),
        ),
    ]