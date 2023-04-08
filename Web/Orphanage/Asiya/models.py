from django.db import models


class Node_Base(models.Model):
    """
    Node name = Node name
    NCV = Node Charge Value

    Node_Class = Node Type (Abstract - 2 | Constant - 1 | Faint - 0)

    Act_Amount = Current Node activation Amount

    ascension_date = Create Data

    last_activation = Last time we changed this Node (Activated)

    """


    node_name = models.CharField(max_lenght=20,verbose_name='Нод',primary_key=True)
    ncv = models.FloatField(verbose_name='Заряд',default=0.0)

    node_class = models.FloatField(verbose_name='Тип Нода',default=0)

    act_amount = models.FloatField(verbose_name='Активации',default=0)

    ascension_date = models.DateTimeField(verbose_name='Дата Формирования',auto_now_add=True)

    last_activation = models.DateTimeField(verbose_name='Последняя Активация',auto_now=True)


    def __str__(self):
        return "%s : %s" % (self.node_name, self.ncv)

    class Meta:
        verbose_name_plural = 'Ноды'
        verbose_name = 'Нод'
        ordering = ['last_activation']


class Pair_Links(models.Model):
    """
    Alpha Node = Core of link
    Beta Node = Tip of link

    Conductivity = Energy loss when activating link

    Force = Energy boost when activating link

    CNLA = Current Node Link Activations

    ascension_date = Create Data

    last_activation = Last time we changed this Node (Activated)

    """

    alpha_node = models.ForeignKey(Node_Base,on_delete=models.CASCADE,verbose_name='Альфа Нод')
    beta_node = models.ForeignKey(Node_Base,on_delete=models.CASCADE,verbose_name='Бета Нод')


    conductivity = models.FloatField(verbose_name='Проводимость',default=0.0)

    force = models.FloatField(verbose_name='Сила',default=0.0)

    cnla = models.FloatField(verbose_name='Активации',default=1)
    

    ascension_date = models.DateTimeField(verbose_name='Дата Формирования',auto_now_add=True)

    last_activation = models.DateTimeField(verbose_name='Последняя Активация',auto_now=True)


    def __str__(self):
        return "%s - %s" % (self.alpha_node, self.beta_node)

    class Meta:
        verbose_name_plural = 'Парные Ноды'
        verbose_name = 'Парный Нод'
        ordering = ['last_activation']


class NL_Base(models.Model):
    
    """
    Base Node = Core of link
    Link branches = Link branch

    """


    base_node = models.OneToOneField(Node_Base,on_delete=models.CASCADE,verbose_name='Нод Основа',primary_key=True)
    link_branches = models.ManyToManyField(Pair_Links,verbose_name='Ветвления Связи')


    def __str__(self):
        return "%s => %s" % (self.base_node, self.link_branches)

    class Meta:
        verbose_name_plural = 'Связи'
        verbose_name = 'Связь'
       




class NG_Base(models.Model):
    """
    NG_Name = Node Group name
    N_Comps = Node Components of Node Group
    NL_Comps = Node Link Components of Node Group

    Status = Completness of NG
    Act_Amount = Activation Amount
    Distribution = Amount of Clusters that contain this Group

    NGX = Node Group X Cord
    NGY = Node Group Y Cord
    NGZ = Node Group Z Cord

    ascension_date = Create Data

    last_activation = Last time we changed this Node (Activated)
    """

    ng_name = models.CharField()
    node_comp = models.ManyToManyField()
    nlinks_comp = models.ManyToManyField()
    

    class Ng_Status(models.TextChoices):
        BROKEN = "Broken", "Неполная"
        COMPLETE = "Complete", "Завершенная"
        FAINTED = "Fainted", "Потухшая"

    #NG_Params
    status = models.CharField() #Choices
    act_amount = models.FloatField()
    distribution = models.FloatField()

    ngx = models.FloatField()
    ngy = models.FloatField()
    ngz = models.FloatField()

    ascension_date = models.DateTimeField(verbose_name='Дата Формирования',auto_now_add=True)

    last_activation = models.DateTimeField(verbose_name='Последняя Активация',auto_now=True)

    def __str__(self):
        return "%s | %s : [%s , %s , %s]" % (self.ng_name, self.status, self.ngx, self.ngy, self.ngz)

    class Meta:
        verbose_name_plural = 'Парные Ноды'
        verbose_name = 'Парный Нод'
        ordering = ['last_activation']
