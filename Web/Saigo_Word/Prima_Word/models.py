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
    
    
    
    group_of_word = models.ForeignKey('GOW',blank=True,null=True,on_delete=models.SET_NULL,
                                      related_name='GOW',verbose_name='Группировка Слов')
   
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



class GOW(models.Model): # Group of Words
    """
    Класс Группировки слов.
    COW = Category Of Words , Категория Слов (Как пример Приветственные)
    """
    cow = models.CharField(max_length = 50,db_index=True,unique=True,verbose_name='Категория Слов')


    def __str__(self):
        return self.cow

    class Meta:
        verbose_name_plural = 'Постоянная Память - Группирование Слов'
        verbose_name = 'Группа'
        ordering = ['cow']



class Sentence_Memory(models.Model): # Память содержащая в себе цельные предложения (В идеале не распознанные)
    """
    Sentence
    Sent_Dech - Дешифрация предложения (Как было сказано в заметках, будет содержать КОД АЙДИ СЛОВ СОДЕРЖАЩИХ)
    Sent_Context
    From_Who
    Short_Mean 
    """
    sentence = models.TextField(db_index=True,unique=True,verbose_name='Предложение')
    sent_dech = models.TextField(verbose_name='Код-Дешифровка предложения')
    sent_context = models.ForeignKey('Context_Table',blank=True,null=True,
                                     on_delete=models.SET_NULL,verbose_name='Контекст предложения')

    x_cord = models.FloatField(verbose_name='X Координата')
    y_cord = models.FloatField(verbose_name='Y Координата')

    special_field = models.CharField(max_length = 150,verbose_name='Спец Поле')

    
    def __str__(self):
        return self.sent_dech

    class Meta:
        verbose_name_plural = 'Постоянная Память - Предложения'
        verbose_name = 'Предложение'
        ordering = ['sentence']



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