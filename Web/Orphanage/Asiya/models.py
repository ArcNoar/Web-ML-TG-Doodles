from django.db import models


# Секция Личностой Памяти - Эмоции
class Ego(models.Model):
    """
    Этот класс содержит данные Асии. Вроде Имени, Возраста, Дня рождения 
    """
    
    appearance = models.ImageField(upload_to='photo/Asiya/%Y/%m/%d',verbose_name='Облик',null=True) #Это в последнюю очередь тип, там сложный момент, потом сделаю.


    first_name = models.CharField(max_length=25,verbose_name='Имя')
    sur_name = models.CharField(max_length=40,verbose_name='Фамилия')
    age = models.FloatField(verbose_name='Возраст',default= 15)
    birthday = models.DateField(blank=True,verbose_name = 'Дата Рождения')

    def __str__(self):
        return "%s %s" % (self.first_name, self.sur_name)

    class Meta:
        verbose_name_plural = 'Фундаментальная Память - Асия'
        verbose_name = 'Данные Асии'


class Person_Memory(models.Model): # Память о существах, и мнение о них.
    """
        Это класс Личностей
        Будет содержать в себе тех кого Асия запомнила, ее отношение к ним, их имя, ну и известные данные
    
        Appearance - Внешность (скорее всего приложен файл будет, правда хер пойми как это будет с тг работать, и как будет работать с сайтом.)
        #TO-DO НУЖНО СДЕЛАТЬ ЭТУ ХУЙНЮ С ВНЕШНКОЙ БРАТАН, ПЕРЕД ЗАПУСКОМ ОБЯЗАЛОВКА БРАТАН. 
    
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
    
    unic_id = models.CharField(max_length = 25,primary_key=True,verbose_name='ID')
    first_name = models.CharField(max_length=25,null=True,verbose_name='Имя')
    sur_name = models.CharField(max_length=40,null=True,verbose_name='Фамилия')
    appearance = models.ImageField(upload_to=f'photo/%Y/%m',verbose_name='Внешний Вид',null=True) #Это в последнюю очередь тип, там сложный момент, потом сделаю.
    birthday = models.DateField(blank=True,null=True,verbose_name = 'Дата Рождения')


    class GenChose(models.TextChoices): #Подкласс для параметра Гендера
        MALE = 'male', 'Мужской'
        NONE_GEN = 'None','Неопределен'
        FEMALE = 'female', 'Женский'

    gender = models.CharField(max_length = 6,verbose_name='Пол',choices=GenChose.choices,default=GenChose.NONE_GEN)
    


    # Репутационный блок - Числовые ЭКВЫ
    #--Положительное отношение

    affection = models.FloatField(default=0.0,null=True,verbose_name='Любовь')
    sympathy = models.FloatField(default=0.0,null=True,verbose_name='Симпатия')
    friendship = models.FloatField(default=0.0,null=True,verbose_name='Дружба')
    admiration = models.FloatField(default=0.0,null=True,verbose_name='Восхищение')
    
    
    #--Спец пункты
    
    mania = models.FloatField(default=0.0,null=True,verbose_name='Мания')

    #--Негативное отношение

    abhorrence = models.FloatField(default=0.0,null=True,verbose_name='Ненависть')
    spite = models.FloatField(default=0.0,null=True,verbose_name='Враждебность')
    disaffection = models.FloatField(default=0.0,null=True,verbose_name='Неприязнь')
    fright = models.FloatField(default=0.0,null=True,verbose_name='Страх')
    


    rep_sum = models.FloatField(null=True,blank=True,
                              verbose_name= 'Балл Взаимоотношений.') # Здесь стоит реализовать розу ветров репутации.

    

        

    # Репутационный блок - Отношение "ОТ" \ "К" кому то 
    # Related Name это спец имя при вызове этой переменной, вообще надо все так сделать, НО ПОИБААААТЬ (простите.)
    relation_to = models.ForeignKey('RelationType',related_name='RelTo', 
                                    on_delete=models.SET_NULL,null=True,verbose_name='Отношение Асии к Сущности:')
    relation_from = models.ForeignKey('RelationType',related_name='RelFrom',
                                      on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Отношение Сущности к Асии:')
    
    
    meet_date = models.DateField(auto_now_add=True,null=True,verbose_name= 'Дата Знакомства')

    fund_description = models.TextField(null=True, blank=True,verbose_name='Краткое Описание')
    local_description = models.TextField(null=True,blank=True,verbose_name='Наблюдения Асии')

    char_1 = models.ForeignKey('Character_Tags',related_name='CharOne',
                               blank=True,on_delete=models.SET_NULL,null=True,verbose_name='Черта Характера (1) - ')
    char_2 = models.ForeignKey('Character_Tags',related_name='CharTwo',
                               blank=True,on_delete=models.SET_NULL,null=True,verbose_name='Черта Характера (2) - ')
    char_3 = models.ForeignKey('Character_Tags',related_name='CharThree',
                               on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Черта Характера (3) - ')
    
    def __str__(self):
        return "%s %s - %s" % (self.first_name, self.sur_name, self.relation_to)
    
    class Meta:
        verbose_name_plural = 'Социальная Память - Личности'
        verbose_name = 'Сущность'
        ordering = ['meet_date']


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
        verbose_name_plural = 'Социальная Память - Взаимотношения'
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
        verbose_name_plural = 'Социальная Память -  Черты Характера'
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
                                      on_delete=models.SET_NULL,verbose_name='Кто Причина')

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
        verbose_name_plural = 'Социальная Память - Архив Эмоций'
        verbose_name = 'Чувство'
        ordering = ['Emote_Name']




# Секция Фундаментальной памяти. (Слова и Предложения)
class VM_Word(models.Model): # Память слов. 
    """
    Verbose Memory - Words
    Секция Фундаментально памяти. Класс Вербальной Памяти - База Данных СЛОВ

    Word = Слово (Будет содежрать в себе слово, не обрезанное) Обязательно сделать праймари Кей.
    Polysemantic = Многозначное или нет? (НЕ ВПЛАНЕ КОНТЕКСТА)
    Constant_W = Это слово константа? (Первородное значение , предназанченное для описания или оценки)
    Word_Type = это слово Действие/Описание/Существительное
    Nomination = Это наименование?

    Associate_W = Ассоциативное Слово(Необязательно)
    Synonym_W = Синоним слова (Необязательно)
    Group_Of_Word = Группа слов, объедянются общим смыслом и назначением

    Word_Des = Описание слова (Необязательно)

    Word_Gender = Род

    """
    word = models.CharField(max_length = 100,db_index=True,unique=True,verbose_name='Слово')
    polysemantic = models.BooleanField(default=False,verbose_name='Многозначность')
    constant_w = models.BooleanField(default=False,verbose_name='Константа')
    nomination = models.BooleanField(default=False,verbose_name='Слово - Наименование?')
    associate_w = models.ForeignKey('VM_Word',blank=True,null=True,on_delete=models.SET_NULL,
                                    related_name='AW',verbose_name='Слово Ассоциация')
    synonym_w = models.ForeignKey('VM_Word',blank=True,null=True,on_delete=models.SET_NULL,
                                  related_name='SynW',verbose_name='Слово Синоним')
    
    group_of_word = models.ForeignKey('GOW',blank=True,null=True,on_delete=models.SET_NULL,
                                      related_name='GOW',verbose_name='Группировка Слов')
   
    class WT_Chose(models.TextChoices): # Подкласс типа слова
        ACTION = 'Motion', 'Глагол'
        ADJECTIVE = 'Descriptor', 'Прилагательное'
        NOUN = 'NOUN', 'Существительное'
        STATE = 'STATE', 'Состояние'
        NOMIN = 'NOMIN', 'Местоимение'
        SOUND = 'SOUND', 'Звук'
        PUNKT = 'PUNCTATION', 'Пунктуация'
        NUM = 'NUM', 'Число'
        UNION = 'UNION', 'Союз'



    word_type = models.CharField(max_length = 16,verbose_name='Тип слова',choices=WT_Chose.choices,default=WT_Chose.NOUN)


    class WGen_Chose(models.TextChoices): # Подкласс рода слова
        MALE = 'Male', 'Мужской'
        NEUTRAL = 'Neutral', 'Средний'
        NONE = 'NONE', 'Без рода'
        FEMALE = 'Female', 'Женский'
    
    word_gender = models.CharField(max_length = 16,verbose_name='Род слова',choices=WGen_Chose.choices,default=WGen_Chose.NONE)

    word_des = models.TextField(blank=True,null=True,verbose_name='Значение слова')

    def __str__(self):
        return "Слово: %s  ||  Тип: %s  ||  Константа: (%s)" % (self.word, self.word_type , self.constant_w)

    class Meta:
        verbose_name_plural = 'Постоянная Память - Вербальная Память'
        verbose_name = 'Слова'
        ordering = ['word']


class GOW(models.Model): # Group of Words
    """
    Класс Группировки слов.
    COW = Category Of Words , Категория Слов (Как пример Приветственные)
    """
    COW = models.CharField(max_length = 50,primary_key=True,verbose_name='Категория Слов')


    def __str__(self):
        return self.COW

    class Meta:
        verbose_name_plural = 'Постоянная Память - Группирование Слов'
        verbose_name = 'Группа'
        ordering = ['COW']




class Sentence_Memory(models.Model): # Память содержащая в себе цельные предложения (В идеале не распознанные)
    """
    Sentence
    Sent_Dech - Дешифрация предложения (Как было сказано в заметках, будет содержать КОД АЙДИ СЛОВ СОДЕРЖАЩИХ)
    Sent_Context
    From_Who
    Short_Mean 
    """
    Sentence = models.TextField(primary_key=True,verbose_name='Предложение')
    Sent_Dech = models.TextField(verbose_name='Код-Дешифровка предложения')
    Sent_Context = models.ForeignKey('Context_Table',blank=True,null=True,
                                     on_delete=models.SET_NULL,verbose_name='Контекст предложения')

    From_Who = models.ForeignKey(Person_Memory,blank=True,null=True,
                                     on_delete=models.SET_NULL,verbose_name='Источник Предложения')

    Short_Mean = models.TextField(blank=True,null=True,verbose_name='Краткая суть')

    def __str__(self):
        return self.Sent_Dech

    class Meta:
        verbose_name_plural = 'Постоянная Память - Предложения'
        verbose_name = 'Предложение'
        ordering = ['Sentence']



class Context_Table(models.Model): # Содержит в себе вероятные контексты сообщения
    """
    (Под контекстом подразумевается (шутка\сарказм\ирония\обман))
    Context
    Context_Desc
    """
    Context = models.CharField(max_length=50,db_index=True,primary_key=True,verbose_name='Контекст')
    Context_Desc = models.TextField(verbose_name='Значение Контекста')



    def __str__(self):
        return self.Context

    class Meta:
        verbose_name_plural = 'Постоянная Память - Контексты'
        verbose_name = 'Контекст'
        ordering = ['Context']





# Секция Фундаментальной памяти. (Воспоминания)


class Semantic_Memory(models.Model): # Обобщенные знания о Мире.
    """
    Класс Памяти содержащий в себе обобщенные знания о Мире.
    Date_Of_Note (DON) - Дата Занесения Знания
    Source_Of_Note (SON) - Источник Занесения Записи (Подразумевается личность, если не от личности то нуль, ну или дефаулт какой та)
    Value_Of_Note (VON) - Ценность Знания (Его достоверность)
    Note - Знание.
    """
    DON = models.DateField(auto_now_add=True,verbose_name='Дата Занесения')
    SON = models.ForeignKey(Person_Memory,on_delete=models.SET_NULL,null=True,blank=True,verbose_name='Источник Записи')
    VON = models.FloatField(default=0.0,verbose_name='Доверие к записи')

    Note = models.TextField(primary_key=True,verbose_name='Запись')

    def __str__(self):
        return "[ %s ] - [ %s ]" % (self.DON, self.SON)
    
    class Meta:
        verbose_name_plural = 'Постоянная Память - Семантическая Память'
        verbose_name = 'Знание'
        ordering = ['DON']


class Constant_Expression(models.Model): # Задаваемые константы (В будещем оспорить)
    """
    Класс содержащий в себе константы, Истинные базы и фундаментальные определения.
    Тут по сути только константа будет описана в качестве Текст филда, хз че еще для консты нужна
    Очень спорный класс, так как сложно занести определенную константу, тип, Убивать плохо? А если убивать лень? И Убивать Кого?
    Const_Expr
    Const_Type
    """
    Const_Expr = models.TextField(primary_key=True,verbose_name='Утверждение')

    class CE_Types(models.TextChoices):
        VERY_GOOD = 'Very_Good', 'Очень Хорошо'
        GOOD = 'Good','Хорошо'
        NEUTRAL = 'Neutral', 'Нейтрально'
        BAD = 'Bad', 'Плохо'
        VERY_BAD = 'Very_Bad', 'Очень плохо'
        


    Const_Type = models.CharField(max_length = 12,verbose_name='Моральная Оценка',choices=CE_Types.choices,default=CE_Types.NEUTRAL)

    def __str__(self):
        return " %s - [ %s ]" % (self.Const_Expr,self.Const_Type)

    class Meta:
        verbose_name_plural = 'Постоянная Память - Константы'
        verbose_name = 'Утверждение'
        ordering = ['Const_Expr']


class Episode_Memory(models.Model): # Эпизодическая Память
    """
    Память фрагментарная. Что то вроде описаний с точки зрений Асии, о ее наблюдениях. Можно сказать ее дневник.
    Я пока хз как это делать, но наверное просто как описательная штука, или краткая заметка, с прикрепленной эмоцией.
    Episode = Воспоминание
    Share_With = С кем разделяет/От кого
    Emote_Score = 
    Date_Of_Recieving(DOR) = Дата приобретения
    Emote_Type = Тип Воспоминания.
    """

    Episode = models.TextField(primary_key=True,verbose_name='Содержание Воспоминания')
    Share_With = models.ForeignKey(Person_Memory,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='С кем разделяет')
    Emote_Score = models.ForeignKey(Emote_Reg,on_delete=models.PROTECT,blank=True,null=True,verbose_name='Испытываемые Эмоции')

    DOR = models.DateField(auto_now_add=True,verbose_name='Дата Приобретения')

    Emote_Type = models.ForeignKey('EM_Type',on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Тип Воспоминания')

    def __str__(self):
        return " %s - [ %s ]" % (self.Emote_Type,self.Share_With)

    class Meta:
        verbose_name_plural = 'Постоянная Память - Эпизодическая Память'
        verbose_name = 'Воспоминание'
        ordering = ['Share_With']

class EM_Type(models.Model): # Тип Эпизодической Памяти.
    """
    Подкласс для категоризации воспоминаний.
    EMT = Тип Эмоции
    """
    EMT = models.CharField(max_length=50,primary_key=True,verbose_name='Тип')
    def __str__(self):
        return self.EMT

    class Meta:
        verbose_name_plural = 'Эпизодичская Память - Тип воспоминания'
        verbose_name = 'Тип'
        ordering = ['EMT']


# Личностная Память ("Я" Асии)

class Identity(models.Model):
    """
    Здесь будет заключены более сложные умозаключения Асии.
    """
    comment = models.TextField(db_index=True,verbose_name='Заключение')

    Emote_Condition = models.ForeignKey(Emote_Reg,on_delete=models.SET_NULL,
                                        blank=True,null=True,verbose_name='Эмоциональнео состояние')

    Current_Motive = models.ForeignKey('Motives',on_delete=models.SET_NULL,
                                        blank=True,null=True,verbose_name='Мотив')

    Reg_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "Синапс - [%s]" % (self.Reg_Date)

    class Meta:
        verbose_name_plural = 'Личностная Память - Эго Асии'
        verbose_name = 'Синапс'
        ordering = ['Reg_Date']


class Motives(models.Model):
    """
    Желания Асии.
    """
    Aspiration = models.TextField(primary_key=True,verbose_name='Стремление')
    Reg_Date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.Aspiration

    class Meta:
        verbose_name_plural = 'Личностная Память - Желания'
        verbose_name = 'Желание'
        ordering = ['Aspiration']


class Postulates(models.Model):
    """
    Постулаты Асии
    """
    Postul = models.TextField(primary_key=True,verbose_name='Постулат')
    Reg_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Postul

    class Meta:
        verbose_name_plural = 'Личностная Память - Постулаты'
        verbose_name = 'Постулат'
        ordering = ['Postul']

class Like_Dislike(models.Model):
    """
    То что нравится\Не нравится Асие
    """
    subject = models.TextField(primary_key=True,verbose_name='Объект')
    Reg_Date = models.DateField(auto_now_add=True)

    class Evaluation(models.TextChoices):
        LIKE = 'Like','Нравится'
        NEUTRAL = 'Neutral', 'Нейтрально'
        DISLIKE = 'Dislike', 'Не нравится'

    rel_to = models.CharField(max_length = 10,verbose_name='Оценка',choices=Evaluation.choices,default=Evaluation.NEUTRAL)

    def __str__(self):
        return " %s - [ %s ]" % (self.subject,self.rel_to)

    class Meta:
        verbose_name_plural = 'Личностная Память - Предпочтения'
        verbose_name = 'Предпочтения'
        ordering = ['subject']