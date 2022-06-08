# Generated by Django 4.0.1 on 2022-05-26 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character_Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('char_tag', models.CharField(db_index=True, max_length=50, verbose_name='Черта Характера.')),
            ],
            options={
                'verbose_name': 'Черта',
                'verbose_name_plural': 'Социальная Память -  Черты Характера',
                'ordering': ['char_tag'],
            },
        ),
        migrations.CreateModel(
            name='Constant_Expression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('const_expr', models.TextField(db_index=True, unique=True, verbose_name='Утверждение')),
                ('const_type', models.CharField(choices=[('Very_Good', 'Очень Хорошо'), ('Good', 'Хорошо'), ('Neutral', 'Нейтрально'), ('Bad', 'Плохо'), ('Very_Bad', 'Очень плохо')], default='Neutral', max_length=12, verbose_name='Моральная Оценка')),
            ],
            options={
                'verbose_name': 'Утверждение',
                'verbose_name_plural': 'Постоянная Память - Константы',
                'ordering': ['const_expr'],
            },
        ),
        migrations.CreateModel(
            name='Context_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(db_index=True, max_length=50, verbose_name='Контекст')),
                ('context_desc', models.TextField(verbose_name='Значение Контекста')),
            ],
            options={
                'verbose_name': 'Контекст',
                'verbose_name_plural': 'Постоянная Память - Контексты',
                'ordering': ['context'],
            },
        ),
        migrations.CreateModel(
            name='Ego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appearance', models.ImageField(null=True, upload_to='photo/Asiya/%Y/%m/%d', verbose_name='Облик')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('sur_name', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('age', models.FloatField(default=15, verbose_name='Возраст')),
                ('birthday', models.DateField(blank=True, verbose_name='Дата Рождения')),
            ],
            options={
                'verbose_name': 'Данные Асии',
                'verbose_name_plural': 'Фундаментальная Память - Асия',
            },
        ),
        migrations.CreateModel(
            name='EM_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emt', models.CharField(db_index=True, max_length=50, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Эпизодичская Память - Тип воспоминания',
                'ordering': ['emt'],
            },
        ),
        migrations.CreateModel(
            name='Emote_Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emote_name', models.CharField(db_index=True, max_length=100, verbose_name='Код Чувства')),
                ('et_type', models.CharField(choices=[('Creature', 'Сущность'), ('None', 'Неопределенный'), ('Ivent', 'Событие'), ('Object', 'Объект')], default='None', max_length=14, verbose_name='Тип Причины')),
                ('et_descript', models.TextField(blank=True, null=True, verbose_name='Описание Причины.')),
                ('et_date', models.DateField(auto_now_add=True, verbose_name='Дата Возникновения')),
                ('horror', models.FloatField(default=0.0, verbose_name='Ужас')),
                ('anxiety', models.FloatField(default=0.0, verbose_name='Тревога')),
                ('concern', models.FloatField(default=0.0, verbose_name='Беспокойство')),
                ('astonishment', models.FloatField(default=0.0, verbose_name='Удивление')),
                ('confusion', models.FloatField(default=0.0, verbose_name='Замешательство')),
                ('timidity', models.FloatField(default=0.0, verbose_name='Робость')),
                ('guilt', models.FloatField(default=0.0, verbose_name='Вина')),
                ('embarrassment', models.FloatField(default=0.0, verbose_name='Смущение')),
                ('doubt', models.FloatField(default=0.0, verbose_name='Сомнение')),
                ('rage', models.FloatField(default=0.0, verbose_name='Ярость')),
                ('irritation', models.FloatField(default=0.0, verbose_name='Раздражение')),
                ('resentment', models.FloatField(default=0.0, verbose_name='Обида')),
                ('disgust', models.FloatField(default=0.0, verbose_name='Отвращение')),
                ('jealousy', models.FloatField(default=0.0, verbose_name='Ревность')),
                ('envy', models.FloatField(default=0.0, verbose_name='Зависть')),
                ('indignation', models.FloatField(default=0.0, verbose_name='Возмущение')),
                ('nervousness', models.FloatField(default=0.0, verbose_name='Нервозность')),
                ('disappointment', models.FloatField(default=0.0, verbose_name='Разочарование')),
                ('idleness', models.FloatField(default=0.0, verbose_name='Лень')),
                ('despait', models.FloatField(default=0.0, verbose_name='Отчаяние')),
                ('compassion', models.FloatField(default=0.0, verbose_name='Жалость')),
                ('loneliness', models.FloatField(default=0.0, verbose_name='Отрешенность')),
                ('helplessness', models.FloatField(default=0.0, verbose_name='Беспомощность')),
                ('aloofness', models.FloatField(default=0.0, verbose_name='Отчужденность')),
                ('regret', models.FloatField(default=0.0, verbose_name='Сожаление')),
                ('boredom', models.FloatField(default=0.0, verbose_name='Скука')),
                ('sadness', models.FloatField(default=0.0, verbose_name='Печаль')),
                ('happiness', models.FloatField(default=0.0, verbose_name='Счастье')),
                ('delight', models.FloatField(default=0.0, verbose_name='Восторг')),
                ('interest', models.FloatField(default=0.0, verbose_name='Интерес')),
                ('excitement', models.FloatField(default=0.0, verbose_name='Возбуждение')),
                ('curiosity', models.FloatField(default=0.0, verbose_name='Любопытство')),
                ('confidence', models.FloatField(default=0.0, verbose_name='Уверенность')),
                ('horny', models.FloatField(default=0.0, verbose_name='Хорни')),
                ('laugh', models.FloatField(default=0.0, verbose_name='Смех')),
                ('satisfaction', models.FloatField(default=0.0, verbose_name='Удовлетворение')),
            ],
            options={
                'verbose_name': 'Чувство',
                'verbose_name_plural': 'Социальная Память - Архив Эмоций',
                'ordering': ['emote_name'],
            },
        ),
        migrations.CreateModel(
            name='GOW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cow', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Категория Слов')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Постоянная Память - Группирование Слов',
                'ordering': ['cow'],
            },
        ),
        migrations.CreateModel(
            name='Like_Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(db_index=True, unique=True, verbose_name='Объект')),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('rel_to', models.CharField(choices=[('Like', 'Нравится'), ('Neutral', 'Нейтрально'), ('Dislike', 'Не нравится')], default='Neutral', max_length=10, verbose_name='Оценка')),
            ],
            options={
                'verbose_name': 'Предпочтения',
                'verbose_name_plural': 'Личностная Память - Предпочтения',
                'ordering': ['subject'],
            },
        ),
        migrations.CreateModel(
            name='Motives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aspiration', models.TextField(db_index=True, unique=True, verbose_name='Стремление')),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Желание',
                'verbose_name_plural': 'Личностная Память - Желания',
                'ordering': ['aspiration'],
            },
        ),
        migrations.CreateModel(
            name='Postulates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postul', models.TextField(db_index=True, unique=True, verbose_name='Постулат')),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Постулат',
                'verbose_name_plural': 'Личностная Память - Постулаты',
                'ordering': ['postul'],
            },
        ),
        migrations.CreateModel(
            name='RelationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation', models.CharField(db_index=True, max_length=50, verbose_name='Тип Отношений.')),
            ],
            options={
                'verbose_name': 'Отношение',
                'verbose_name_plural': 'Социальная Память - Взаимотношения',
                'ordering': ['relation'],
            },
        ),
        migrations.CreateModel(
            name='VM_Alph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('construct', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Слово')),
                ('alp_t', models.CharField(choices=[('LETTER', 'Кириллица'), ('ENG_LET', 'Латинница'), ('NOMIN', 'Местоимение'), ('INTER', 'Междометие'), ('UNION', 'Союз'), ('PREPOS', 'Предлог'), ('PUNCTATION', 'Пунктуация'), ('NUM', 'Число'), ('SYMBOL', 'Символ'), ('SMILE', 'Смайл'), ('NONE_T', 'Не имеется')], default='LETTER', max_length=16, verbose_name='Тип ')),
                ('alp_t2', models.CharField(choices=[('LETTER', 'Кириллица'), ('ENG_LET', 'Латинница'), ('NOMIN', 'Местоимение'), ('INTER', 'Междометие'), ('UNION', 'Союз'), ('PREPOS', 'Предлог'), ('PUNCTATION', 'Пунктуация'), ('NUM', 'Число'), ('SYMBOL', 'Символ'), ('SMILE', 'Смайл'), ('NONE_T', 'Не имеется')], default='NONE_T', max_length=16, verbose_name='Тип 2')),
            ],
            options={
                'verbose_name': 'Конструкт',
                'verbose_name_plural': 'Постоянная Память - Конструкты',
                'ordering': ['alp_t'],
            },
        ),
        migrations.CreateModel(
            name='VM_Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(db_index=True, max_length=100, unique=True, verbose_name='Слово')),
                ('word_code', models.CharField(max_length=100, verbose_name='Код')),
                ('word_type', models.CharField(choices=[('VERB', 'Глагол'), ('ADJECTIVE', 'Прилагательное'), ('NOUN', 'Существительное'), ('STATE', 'Наречие'), ('NOMIN', 'Местоимение'), ('INTER', 'Междометие'), ('PRICH', 'Причастие'), ('DEPRICH', 'Деепричастие'), ('UNION', 'Союз'), ('PARTIC', 'Частица'), ('PREPOS', 'Предлог'), ('NUMIN', 'Числительное'), ('PREDICAT', 'Предикатив'), ('PUNCTATION', 'Пунктуация'), ('NUM', 'Число'), ('SYMBOL', 'Символ'), ('SMILE', 'Смайл'), ('NONE_T', 'Не имеется')], default='NOUN', max_length=16, verbose_name='Тип слова')),
                ('word_des', models.TextField(blank=True, null=True, verbose_name='Значение слова')),
                ('group_of_word', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='GOW', to='Asiya.gow', verbose_name='Группировка Слов')),
            ],
            options={
                'verbose_name': 'Слова',
                'verbose_name_plural': 'Постоянная Память - Вербальная Память',
                'ordering': ['word'],
            },
        ),
        migrations.CreateModel(
            name='User_Memory',
            fields=[
                ('unic_id', models.CharField(max_length=25, unique=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, null=True, verbose_name='Имя')),
                ('sur_name', models.CharField(max_length=40, null=True, verbose_name='Фамилия')),
                ('appearance', models.ImageField(null=True, upload_to='photo/%Y/%m', verbose_name='Внешний Вид')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата Рождения')),
                ('perms', models.CharField(choices=[('Absolute', 'Абсолют.'), ('High_Perm', 'Афелий.'), ('Mid_Perm', 'Апсид.'), ('Low_Perm', 'Перигелий.'), ('Zero_Perm', 'Zero.')], default='Zero_Perm', max_length=18, verbose_name='Права')),
                ('login', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Login')),
                ('password', models.CharField(max_length=38, verbose_name='Password')),
                ('gender', models.CharField(choices=[('male', 'Мужской'), ('None', 'Неопределен'), ('female', 'Женский')], default='None', max_length=6, verbose_name='Пол')),
                ('affection', models.FloatField(default=0.0, null=True, verbose_name='Любовь')),
                ('sympathy', models.FloatField(default=0.0, null=True, verbose_name='Симпатия')),
                ('friendship', models.FloatField(default=0.0, null=True, verbose_name='Дружба')),
                ('admiration', models.FloatField(default=0.0, null=True, verbose_name='Восхищение')),
                ('mania', models.FloatField(default=0.0, null=True, verbose_name='Мания')),
                ('abhorrence', models.FloatField(default=0.0, null=True, verbose_name='Ненависть')),
                ('spite', models.FloatField(default=0.0, null=True, verbose_name='Враждебность')),
                ('disaffection', models.FloatField(default=0.0, null=True, verbose_name='Неприязнь')),
                ('fright', models.FloatField(default=0.0, null=True, verbose_name='Страх')),
                ('rep_sum', models.FloatField(blank=True, null=True, verbose_name='Балл Взаимоотношений.')),
                ('meet_date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата Знакомства')),
                ('fund_description', models.TextField(blank=True, null=True, verbose_name='Краткое Описание')),
                ('local_description', models.TextField(blank=True, null=True, verbose_name='Наблюдения Асии')),
                ('char_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CharOne', to='Asiya.character_tags', verbose_name='Черта Характера (1) - ')),
                ('char_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CharTwo', to='Asiya.character_tags', verbose_name='Черта Характера (2) - ')),
                ('char_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='CharThree', to='Asiya.character_tags', verbose_name='Черта Характера (3) - ')),
                ('relation_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RelFrom', to='Asiya.relationtype', verbose_name='Отношение Сущности к Асии:')),
                ('relation_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='RelTo', to='Asiya.relationtype', verbose_name='Отношение Асии к Сущности:')),
            ],
            options={
                'verbose_name': 'Сущность',
                'verbose_name_plural': 'Социальная Память - Личности',
                'ordering': ['meet_date'],
            },
        ),
        migrations.CreateModel(
            name='Sentence_Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.TextField(db_index=True, unique=True, verbose_name='Предложение')),
                ('sent_dech', models.TextField(verbose_name='Код-Дешифровка предложения')),
                ('short_mean', models.TextField(blank=True, null=True, verbose_name='Краткая суть')),
                ('from_who', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asiya.user_memory', verbose_name='Источник Предложения')),
                ('sent_context', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asiya.context_table', verbose_name='Контекст предложения')),
            ],
            options={
                'verbose_name': 'Предложение',
                'verbose_name_plural': 'Постоянная Память - Предложения',
                'ordering': ['sentence'],
            },
        ),
        migrations.CreateModel(
            name='Semantic_Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('don', models.DateField(auto_now_add=True, verbose_name='Дата Занесения')),
                ('von', models.FloatField(default=0.0, verbose_name='Доверие к записи')),
                ('note', models.TextField(db_index=True, unique=True, verbose_name='Запись')),
                ('son', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asiya.user_memory', verbose_name='Источник Записи')),
            ],
            options={
                'verbose_name': 'Знание',
                'verbose_name_plural': 'Постоянная Память - Семантическая Память',
                'ordering': ['don'],
            },
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(db_index=True, verbose_name='Заключение')),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('current_motive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asiya.motives', verbose_name='Мотив')),
                ('emote_condition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asiya.emote_reg', verbose_name='Эмоциональнео состояние')),
            ],
            options={
                'verbose_name': 'Синапс',
                'verbose_name_plural': 'Личностная Память - Эго Асии',
                'ordering': ['reg_date'],
            },
        ),
        migrations.CreateModel(
            name='Episode_Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode', models.TextField(db_index=True, unique=True, verbose_name='Содержание Воспоминания')),
                ('dor', models.DateField(auto_now_add=True, verbose_name='Дата Приобретения')),
                ('emote_score', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Asiya.emote_reg', verbose_name='Испытываемые Эмоции')),
                ('emote_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asiya.em_type', verbose_name='Тип Воспоминания')),
                ('share_with', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asiya.user_memory', verbose_name='С кем разделяет')),
            ],
            options={
                'verbose_name': 'Воспоминание',
                'verbose_name_plural': 'Постоянная Память - Эпизодическая Память',
                'ordering': ['share_with'],
            },
        ),
        migrations.AddField(
            model_name='emote_reg',
            name='emote_trigger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ETrig', to='Asiya.user_memory', verbose_name='Кто Причина'),
        ),
    ]
