# Generated by Django 4.0.1 on 2022-02-17 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asiya', '0008_rename_friendship_person_memory_friendship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context_table',
            name='Context',
            field=models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False, verbose_name='Контекст'),
        ),
        migrations.AlterField(
            model_name='gow',
            name='COW',
            field=models.CharField(db_index=True, max_length=50, primary_key=True, serialize=False, verbose_name='Категория Слов'),
        ),
        migrations.AlterField(
            model_name='person_memory',
            name='appearance',
            field=models.ImageField(null=True, upload_to='photo/%Y/%m', verbose_name='Внешний Вид'),
        ),
        migrations.AlterField(
            model_name='vm_word',
            name='Word',
            field=models.CharField(db_index=True, max_length=100, primary_key=True, serialize=False, verbose_name='Слово'),
        ),
    ]