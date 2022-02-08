from django.db import models



class Ego(models.Model):
    """
    Этот класс содержит данные Асии. Вроде Имени, Возраста, Дня рождения 
    """
    #Appearance = models.ImageField() #Это в последнюю очередь тип, там сложный момент, потом сделаю.


    first_name = models.CharField(max_length=25,verbose_name='Имя')
    sur_name = models.CharField(max_length=40,verbose_name='Фамилия')
    age = models.FloatField(verbose_name='Возраст',default= 15)
    birthday = models.DateField(blank=True,verbose_name = 'Дата Рождения')

    def __str__(self):
        return "%s %s" % (self.first_name, self.sur_name)

    class Meta:
        verbose_name_plural = 'Биография'
        verbose_name = 'Данные Асии'


class Person_Memory(models.Model): # Память о существах, и мнение о них.
    """
        Это класс Личностей
        Будет содержать в себе тех кого Асия запомнила, ее отношение к ним, их имя, ну и известные данные
    
        Appearance - Внешность (скорее всего приложен файл будет, правда хер пойми как это будет с тг работать, и как будет работать с сайтом.)
    
    
        unic_id - Поскольку этот сайт по сути является оболочкой, будем брать айдишник пользователя с телеграм канала.
        first_name - Имя
        sur_name - Фамилия
        birthday - Дата рождения
        gender - Пол
    
        Species - Расса (*была удалена*)
    
    Rep_SUM - (Репутация В числовом Экв) Наверное это будет показателм ощущения комфорта ?
        Тут будет список эквивалентов: (Количество знаком это сила воздействия к коэффиценту влияния репутации.)
            Affection - Любовь (+++++)
            Sympathy - Симпатия (++++)
            FriendShip - Дружба (+++)
            Admiration - Восхищение (++)
            Interest - Интерес (+) (Удалено)

            Mania - Мания (Должна влиять на установку пункта зависимости.)


            Abhorrence - Ненависть\Отторжение (-----)
            Spite - Злоба\Враждебность (----)
            DisAffection - Неприязнь\Недружелюбность (---)
            Fright - Страх (--)
            Ennui -  Тоска(Скука) по отношению к объетку(-) (Удалено)




    Relation_To - (Как Асия относится к Юниту)
    Relation_From - (Как Юнит относится к Асии)
    Meet_Date - (Дата встречи)
    
    Fund_Description - Описание занесенное пользователем
    Local_Description - Описание подмеченное асией
    
    Самые выделяющиеся черты характера
    Char_1 - Черта характера присвоенная Асией 
    Char_2 - Черта Характера Присвоенная Асией
    Char_3 - Черта Характера Присвоенная Асией

    """
    #Appearance = models.ImageField() #Это в последнюю очередь тип, там сложный момент, потом сделаю.
    
    unic_id = models.CharField(max_length = 25,primary_key=True,verbose_name='ID')
    first_name = models.CharField(max_length=25,verbose_name='Имя')
    sur_name = models.CharField(max_length=40,verbose_name='Фамилия')
    birthday = models.DateField(blank=True,verbose_name = 'Дата Рождения')


    class GenChose(models.TextChoices): #Подкласс для параметра Гендера
        MALE = 'male', 'Мужской'
        NONE_GEN = 'None','Неопределен'
        FEMALE = 'female', 'Женский'

    gender = models.CharField(max_length = 6,verbose_name='Пол',choices=GenChose.choices,default=GenChose.NONE_GEN)
    


    # Репутационный блок - Числовые ЭКВЫ
    #--Положительное отношение

    Affection = models.FloatField(default=0.0,verbose_name='Любовь')
    Sympathy = models.FloatField(default=0.0,verbose_name='Симпатия')
    FriendShip = models.FloatField(default=0.0,verbose_name='Дружба')
    Admiration = models.FloatField(default=0.0,verbose_name='Восхищение')
    
    
    #--Спец пункты
    
    Mania = models.FloatField(default=0.0,verbose_name='Мания')

    #--Негативное отношение

    Abhorrence = models.FloatField(default=0.0,verbose_name='Ненависть')
    Spite = models.FloatField(default=0.0,verbose_name='Враждебность')
    DisAffection = models.FloatField(default=0.0,verbose_name='Неприязнь')
    Fright = models.FloatField(default=0.0,verbose_name='Страх')
    


    Rep_SUM = models.FloatField(null=True,blank=True,
                              verbose_name= 'Балл Взаимоотношений.') # Здесь стоит реализовать розу ветров репутации.

    

        

    # Репутационный блок - Отношение "ОТ" \ "К" кому то 
    # Related Name это спец имя при вызове этой переменной, вообще надо все так сделать, НО ПОИБААААТЬ (простите.)
    Relation_To = models.ForeignKey('RelationType',related_name='RelTo', 
                                    on_delete=models.PROTECT,verbose_name='Отношение Асии к Сущности:')
    Relation_From = models.ForeignKey('RelationType',related_name='RelFrom',
                                      on_delete=models.PROTECT,blank=True,null=True,verbose_name='Отношение Сущности к Асии:')
    
    
    Meet_Date = models.DateField(auto_now_add=True,verbose_name= 'Дата Знакомства')

    Fund_Description = models.TextField(null=True, blank=True,verbose_name='Краткое Описание')
    Local_Description = models.TextField(null=True,blank=True,verbose_name='Наблюдения Асии')

    Char_1 = models.ForeignKey('Character_Tags',related_name='CharOne',
                               blank=True,on_delete=models.PROTECT,null=True,verbose_name='Черта Характера (1) - ')
    Char_2 = models.ForeignKey('Character_Tags',related_name='CharTwo',
                               blank=True,on_delete=models.PROTECT,null=True,verbose_name='Черта Характера (2) - ')
    Char_3 = models.ForeignKey('Character_Tags',related_name='CharThree',
                               on_delete=models.PROTECT,blank=True,null=True,verbose_name='Черта Характера (3) - ')
    
    def __str__(self):
        return "%s %s - %s" % (self.first_name, self.sur_name, self.Relation_To)
    
    class Meta:
        verbose_name_plural = 'Личностная Память'
        verbose_name = 'Сущность'
        ordering = ['Meet_Date']


class RelationType(models.Model): # Класс содержащий виды Взаимоотношений.
    """
    Класс Взаимотношений ОТ\К
    - Relation - 
    """
    Relation = models.CharField(max_length=50,db_index=True,
                                verbose_name = 'Тип Отношений.')
    def __str__(self):
        return self.Relation

    class Meta:
        verbose_name_plural = 'Взаимотношения'
        verbose_name = 'Отношение'
        ordering = ['Relation']

class Character_Tags(models.Model): # Класс Черт характера.
    """
    Класс черт характера.
    """
    char_tag = models.CharField(max_length=50,db_index=True,
                                verbose_name='Черта Характера.')
    def __str__(self):
        return self.char_tag
    
    class Meta:
        verbose_name_plural = 'Черты Характера'
        verbose_name = 'Черта'
        ordering = ['char_tag']





class Emote_Reg(models.Model): # Эмоциональное состояние
    """
    Началом этого кода всегда должно быть слово - Фундаментальная эмоция. [Happy - *Код*]
    Emote_Name = Должен содержать в себе своеобразный генокод (Литералы Эмоций подряд) ('HFAH ... SAH')

    Emote_Trigger = Кто вызвал подобную эмоцию (Если Сущность, в противном случае оставить NULL)
    ET_Type = тип триггера  (Сущность, Объект, Событие)
    ET_Descript = Описаение триггера (Короткая заметка, о том какой объект или событие, 
                                            можно оставить пустым если вызвала Сущность)
    ET_Date - Дата Триггера (Необязательна к заполнению, хотя скорее всего я вообще авто дату сделаю.)


    """
    
    Emote_Name = models.CharField(max_length=100, db_index=True,
                            verbose_name= 'Код Чувства')
    
    # Описательные переменные
    Emote_Trigger = models.ForeignKey(Person_Memory,related_name='ETrig',blank=True,null=True,
                                      on_delete=models.PROTECT,verbose_name='Кто Причина')

    class ET_TypeChose(models.TextChoices): #Подкласс для параметра типа
        CREATURE = 'Creature', 'Сущность'
        ET_NONE = 'None','Неопределенный'
        IVENT = 'Ivent','Событие'
        OBJECT = 'Object', 'Объект'

    ET_Type = models.CharField(max_length = 14,verbose_name='Тип Причины',choices=ET_TypeChose.choices,default=ET_TypeChose.ET_NONE)
    ET_Descript = models.TextField(null=True, blank=True,verbose_name='Описание Причины.')

    ET_Date = models.DateField(auto_now_add= True,verbose_name= 'Дата Возникновения')

    # Компоненты Чувств.
    # СТРАХ :
    """
        1 Horror = Ужас
        2 Anxiety =  = Тревога
        3 Concern = Беспокойство
        4 Astonishment =  Удивление
        5 Confusion = Замешательство
        6 Timidity = Робость
        7 Guilt = Вина
        8 Embarrassment = Смущение
        9 Doubt = Сомнение
     """
    Horror = models.FloatField(default=0.0,verbose_name='Ужас')
    Anxiety = models.FloatField(default=0.0,verbose_name='Тревога')
    Concern = models.FloatField(default=0.0,verbose_name='Беспокойство')
    Astonishment = models.FloatField(default=0.0,verbose_name='Удивление')
    Confusion = models.FloatField(default=0.0,verbose_name='Замешательство')
    Timidity = models.FloatField(default=0.0,verbose_name='Робость')
    Guilt = models.FloatField(default=0.0,verbose_name='Вина')
    Embarrassment = models.FloatField(default=0.0,verbose_name='Смущение')
    Doubt = models.FloatField(default=0.0,verbose_name='Сомнение')

    
    #ГНЕВ :
    """
        1 Rage = Ярость
        2 Irritation = Раздражение
        3 Resentment = Обида
        4 Disgust = Отвращение\Презрительное
        5 Jealousy = Ревность
        6 Envy = Зависть
        7 Indignation = Негодование/Возмущение
        8 Nervousness = Нервозность
        9 Disappointment = Разочарование
    """
    Rage = models.FloatField(default=0.0,verbose_name='Ярость')
    Irritation = models.FloatField(default=0.0,verbose_name='Раздражение')
    Resentment = models.FloatField(default=0.0,verbose_name='Обида')
    Disgust = models.FloatField(default=0.0,verbose_name='Отвращение')
    Jealousy = models.FloatField(default=0.0,verbose_name='Ревность')
    Envy = models.FloatField(default=0.0,verbose_name='Зависть')
    Indignation = models.FloatField(default=0.0,verbose_name='Возмущение')
    Nervousness = models.FloatField(default=0.0,verbose_name='Нервозность')
    Disappointment = models.FloatField(default=0.0,verbose_name='Разочарование')


    #ГРУСТЬ:
    """
        1 Idleness = Лень
        2 Despait = Отчаяние
        3 Compassion = Жалость
        4 Loneliness = Отрешенность/Одиночество
        5 Helplessness = Беспомощность
        6 Aloofness = Отчужденность
        7 Regret = Сожаление
        8 Boredom = Скука
        9 Sadness = Печаль
    """
    Idleness = models.FloatField(default=0.0,verbose_name='Лень')
    Despait = models.FloatField(default=0.0,verbose_name='Отчаяние')
    Compassion = models.FloatField(default=0.0,verbose_name='Жалость')
    Loneliness = models.FloatField(default=0.0,verbose_name='Отрешенность')
    Helplessness = models.FloatField(default=0.0,verbose_name='Беспомощность')
    Aloofness = models.FloatField(default=0.0,verbose_name='Отчужденность')
    Regret = models.FloatField(default=0.0,verbose_name='Сожаление')
    Boredom = models.FloatField(default=0.0,verbose_name='Скука')
    Sadness = models.FloatField(default=0.0,verbose_name='Печаль')

    #РАДОСТЬ :
    """
        1 Happiness = Счастье
        2 Delight =  Восторг
        3 Interest = Интерес
        4 Excitement = Возбуждение
        5 Curiosity = Любопытство
        6 Confidence = Уверенность
        7 Horny = Возбуждение(хорни)
        8 Laugh = Смех
        9 Satisfaction = Удовлетворение
    """
    Happiness = models.FloatField(default=0.0,verbose_name='Счастье')
    Delight = models.FloatField(default=0.0,verbose_name='Восторг')
    Interest = models.FloatField(default=0.0,verbose_name='Интерес')
    Excitement = models.FloatField(default=0.0,verbose_name='Возбуждение')
    Curiosity = models.FloatField(default=0.0,verbose_name='Любопытство')
    Confidence = models.FloatField(default=0.0,verbose_name='Уверенность')
    Horny = models.FloatField(default=0.0,verbose_name='Хорни')
    Laugh = models.FloatField(default=0.0,verbose_name='Смех')
    Satisfaction = models.FloatField(default=0.0,verbose_name='Удовлетворение')



    def __str__(self):
        return "КОД: %s  ||  Причина: %s  ||  Дата: (%s)" % (self.Emote_Name, self.Emote_Trigger, self.ET_Date)

    class Meta:
        verbose_name_plural = 'Архив Эмоций'
        verbose_name = 'Чувство'
        ordering = ['Emote_Name']

