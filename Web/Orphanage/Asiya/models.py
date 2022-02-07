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
            Interest - Интерес (+)

            Mania - Мания (Должна влиять на установку пункта зависимости.)


            Abhorrence - Ненависть\Отторжение (-----)
            Spite - Злоба\Враждебность (----)
            DisAffection - Неприязнь\Недружелюбность (---)
            Fright - Страх (--)
            Ennui -  Тоска(Скука) по отношению к объетку(-)




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
    Interest = models.FloatField(default=0.0,verbose_name='Интерес')
    
    #--Спец пункты
    
    Mania = models.FloatField(default=0.0,verbose_name='Мания')

    #--Негативное отношение

    Abhorrence = models.FloatField(default=0.0,verbose_name='Ненависть')
    Spite = models.FloatField(default=0.0,verbose_name='Враждебность')
    DisAffection = models.FloatField(default=0.0,verbose_name='Неприязнь')
    Fright = models.FloatField(default=0.0,verbose_name='Страх')
    Ennui = models.FloatField(default=0.0,verbose_name='Тоска')


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
        return "%s %s" % (self.first_name, self.sur_name)
    
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


class EmoState(models.Model): # Эмоциональное состояние
    """
    ЭТОТ КЛАСС НЕ ГОТОВ, НИЖЕ СТОЯЩЕЕ МУСОР, Я ГИТА, ВЫШЕ СТОЯЩИЕ ШТУКИ.
    """
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name= 'Вид Объекта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Типизация'
        verbose_name = 'Представление'
        ordering = ['name']

