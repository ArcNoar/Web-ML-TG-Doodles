# Generated by Django 4.0.1 on 2022-02-15 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asiya', '0006_alter_person_memory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person_memory',
            old_name='telation_from',
            new_name='relation_from',
        ),
    ]