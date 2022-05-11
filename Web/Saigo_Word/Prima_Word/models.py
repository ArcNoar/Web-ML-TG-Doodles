from django.db import models

# Create your models here.
class VM_Alph(models.Model):
    construct = models.CharField(max_length = 100,db_index=True,unique=True,verbose_name='Слово')
    
    
   
    class CT_Chose(models.TextChoices): # Подкласс типа Конструкта
        
        LETTER = 'LETTER', 'Кириллица'
        ENG_LET = 'ENG_LET', 'Латинница'

        NOMIN = 'NOMIN', 'Местоимение'
        INTER = 'INTER', 'Междометие'
        UNION = 'UNION', 'Союз'
        PREPOS = 'PREPOS', 'Предлог'

        PUNKT = 'PUNCTATION', 'Пунктуация'
        NUM = 'NUM', 'Число'
        SYMBOL = 'SYMBOL', 'Символ'
        SMILE = 'SMILE', 'Смайл'

        NONE_T = 'NONE_T', 'Не имеется'



    alp_t = models.CharField(max_length = 16,verbose_name='Тип ',choices=CT_Chose.choices,default=CT_Chose.LETTER)
    #alp_t2 = models.CharField(max_length = 16,verbose_name='Тип 2',choices=CT_Chose.choices,default=CT_Chose.NONE_T)


    

    def __str__(self):
        return "Конструкт: %s  ||  Тип: %s  ||" % (self.construct, self.alp_t )

    class Meta:
        verbose_name_plural = 'Постоянная Память - Конструкты'
        verbose_name = 'Конструкт'
        ordering = ['alp_t']


class VM_Word(models.Model): # Память слов. 
    """
   

    """
    word = models.CharField(max_length = 100,db_index=True,unique=True,verbose_name='Слово')
    word_code = models.CharField(max_length = 100,verbose_name='Код')
    
    
    
    #group_of_word = models.ForeignKey('GOW',blank=True,null=True,on_delete=models.SET_NULL,
    #                                  related_name='GOW',verbose_name='Группировка Слов')
   
    x_cord = models.FloatField(verbose_name='X Координата')
    y_cord = models.FloatField(verbose_name='Y Координата')

    special_field = models.CharField(max_length = 150,verbose_name='Спец Поле')

    class WT_Chose(models.TextChoices): # Подкласс типа слова
        VERB = 'VERB', 'Глагол'
        ADJECTIVE = 'ADJECTIVE', 'Прилагательное'
        NOUN = 'NOUN', 'Существительное'
        ADVERB = 'STATE', 'Наречие'
        NOMIN = 'NOMIN', 'Местоимение'
        INTER = 'INTER', 'Междометие'
        UNION = 'UNION', 'Союз'
        PREPOS = 'PREPOS', 'Предлог'
        NUMIN = 'NUMIN', 'Числительное'
        PTICK = 'PTICK', 'Частица'
        PRICH = 'PRICH', 'причастие'
        DEPRICH = 'DEPRICH', 'деепричастие'

        PUNKT = 'PUNCTATION', 'Пунктуация'
        NUM = 'NUM', 'Число'
        SYMBOL = 'SYMBOL', 'Символ'
        NAME = 'NAME', 'Имя'

        NONE_T = 'NONE_T', 'Не имеется'



    word_type = models.CharField(max_length = 20,verbose_name='Часть Речи',choices=WT_Chose.choices,default=WT_Chose.NONE_T)
    

    def __str__(self):
        return "Слово: %s  ||  Тип: %s ||" % (self.word, self.word_type)

    class Meta:
        verbose_name_plural = 'Хранилище Слов'
        verbose_name = 'Слова'
        ordering = ['word_type']




"""
class Sentence_Memory(models.Model): # Память содержащая в себе цельные предложения (В идеале не распознанные)
    
    sentence = models.TextField(db_index=True,unique=True,verbose_name='Предложение')
    sent_dech = models.TextField(verbose_name='Код-Дешифровка предложения')
    sent_context = models.ForeignKey('Context_Table',blank=True,null=True,
                                     on_delete=models.SET_NULL,verbose_name='Контекст предложения')

    group_of_sent = models.ForeignKey('GOS',blank=True,null=True,on_delete=models.SET_NULL,
                                      related_name='GOS',verbose_name='Категории Предложений')

    x_cord = models.FloatField(verbose_name='X Координата')
    y_cord = models.FloatField(verbose_name='Y Координата')

    special_field = models.CharField(max_length = 150,verbose_name='Спец Поле')

    
    def __str__(self):
        return self.sent_dech

    class Meta:
        verbose_name_plural = 'Постоянная Память - Предложения'
        verbose_name = 'Предложение'
        ordering = ['sentence']
"""

class Correct_Answers(models.Model):

    user_sent = models.TextField(verbose_name='Предложение Пользователя')

    us_dech = models.TextField(verbose_name='Код-Дешифровка US')

    actual_resp = models.TextField(db_index=True,verbose_name='Корректный Ответ.')

    ar_dech = models.TextField(verbose_name='Код-Дешифровка AR')

    category = models.ForeignKey('GOS',blank=True,null=True,on_delete=models.SET_NULL,
                                      related_name='GOS',verbose_name='Категория')

    sent_context = models.ForeignKey('Context_Table',blank=True,null=True,
                                     on_delete=models.SET_NULL,verbose_name='Контекст')

    g1 = models.FloatField(default=5.0,null=False,verbose_name='Структура')

    g2 = models.FloatField(default=5.0,null=False,verbose_name='Грамматика')

    g3 = models.FloatField(default=10.0,null=False,verbose_name='Локальная Универсальность')

    g4 = models.FloatField(default=10.0,null=False,verbose_name='Глобальная Универсальность')

    g5 = models.FloatField(default=10.0,null=False,verbose_name='МоноРезистентность')

    g6 = models.FloatField(default=5.0,null=False,verbose_name='Осмысленность')

    g7 = models.BooleanField(default=False,null=False,verbose_name='Завершенность')

    g8 = models.BooleanField(default=False,null=False,verbose_name='Гибкая Дополняемость.')


    def __str__(self):
        return "US: %s  ||  AR: %s ||" % (self.user_sent, self.actual_resp)

    class Meta:
        verbose_name_plural = 'Постоянная Память - Корректные предложения.'
        verbose_name = 'Предложение'
        ordering = ['category']


class GOS(models.Model): # Group of Words
    """
    Класс Группировки Sentence.
    COS = Category Of Sentences , Категория Sentence (Как пример Приветственные)
    """
    cos = models.CharField(max_length = 50,db_index=True,unique=True,verbose_name='Категория Слов')


    def __str__(self):
        return self.cos

    class Meta:
        verbose_name_plural = 'Постоянная Память - Категории Предложений.'
        verbose_name = 'Группа'
        ordering = ['cos']


class Context_Table(models.Model): # Содержит в себе вероятные контексты сообщения
    """
    (Под контекстом подразумевается (шутка\сарказм\ирония\обман))
    Context
    Context_Desc
    """
    context = models.CharField(max_length=50,db_index=True,verbose_name='Контекст')
    



    def __str__(self):
        return self.context

    class Meta:
        verbose_name_plural = 'Постоянная Память - Контексты'
        verbose_name = 'Контекст'
        ordering = ['context']