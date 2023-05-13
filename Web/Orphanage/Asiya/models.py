from pyexpat import model
from django.db import models


class Node_Base(models.Model): #Nodes data and Their Links
    """
    Node name = Node Name
    NCV = Node Charge Value
    Node_Class = Node Type (Abstract - 2 | Constant - 1 | Faint - 0)
        Abstract - We can't associated value, it's complexity of constant nodes or higher units (Not same as Group)
        Constant - It's always have some associated value behind it (Digits, Letters)
        Faint - Node with low charge (It's can't create reaction with other nodes, but can be activated by other nodes)

    Act_Amount = Current Node Activation Amount
    Ascension_Date = Create Data
    Last Activation = Last time this node was triggered / interacted / changed
    """

    node_name = models.CharField(max_length=20,verbose_name='Нод',primary_key=True)
    ncv = models.FloatField(verbose_name='Заряд', default=0.0)
    node_class = models.FloatField(verbose_name="Тип Нода", default=0)
    act_amount = models.FloatField(verbose_name='Активации',default=1)
    ascension_date = models.DateTimeField(verbose_name="Дата Формирования", auto_now_add=True, null=True)
    last_activation = models.DateTimeField(verbose_name='Последняя Активация', auto_now_add=True,null=True)

    def __str__(self):
        return "%s : %s" % (self.node_name, self.ncv)
    
    class Meta:
        verbose_name_plural = 'Ноды'
        verbose_name = 'Нод'
        ordering = ['last_activation']


class Node_Link_Base(models.Model): #Node Links Data
    """
    Alpha Node = Core of Link
    Beta Node = Endpoint Link
    Conductivity = Energy Loss when activating link 
    Force = Energy boost when activating link
    CNLA = Current Node Link Activations
    Ascension_date = Create Date
    last_activation = Last time this link was triggered / interacted / changed
    """

    alpha_node = models.ForeignKey(Node_Base,related_name='Link_Alpha_Node', on_delete=models.CASCADE, verbose_name="Альфа Нод")
    beta_node = models.ForeignKey(Node_Base,related_name='Link_Beta_Node', on_delete=models.CASCADE, verbose_name="Бета Нод")

    conductivity = models.FloatField(verbose_name='Проводимость',default=0.0)
    force = models.FloatField(verbose_name='Сила',default=0.0)
    cnla = models.FloatField(verbose_name='Активации',default=1)

    ascension_date = models.DateTimeField(verbose_name='Дата Формирование',auto_now_add=True)
    last_activation = models.DateTimeField(verbose_name='Последняя Активация',auto_now=True)


    def __str__(self):
        return "Node [%s] - Node [%s]" % (self.alpha_node, self.beta_node)

    class Meta:
        verbose_name_plural = 'Нод Связи'
        verbose_name = 'Нод Связь'
        ordering = ['last_activation']

# NG_Base is some kind of empty shell that makes abstraction easier to understand
# NGCL is the main part of Node Group, it contains Nodes and Links that formed our group

class NGCL(models.Model):
    """
    This NGCL can be reused if there is word that have same links and nodes.
    NGCL = Node Group Construct List
    - NG_Code (Should contain in name, nodes key, and links pairs)
    - NCL(Node Constructs List)
    - NLCL(Node Link Construct list) 
    """

    ng_code = models.CharField(max_length=200, verbose_name='Код Группы', primary_key=True)
    ncl = models.ManyToManyField(Node_Base,related_name='Node_Construct_List',verbose_name="Конструкт Лист Нодов")
    nlcl = models.ManyToManyField(Node_Link_Base,related_name='Node_Link_Construct_List',verbose_name="Конструкт Лист Нод Линков")

    def __str__(self):
        return "NG Code [%s]" % (self.ng_code)

    class Meta:
        verbose_name_plural = 'Конструкты Нод Группы'
        verbose_name = 'Конструкт Нод Группы'
        ordering = ['ng_code']


class NG_Base(models.Model):
    """
    GN = Group Name
    NGCL = Node Group Construct List :
    - NCL(Node Constructs List)
    - NLCL(Node Link Construct list)
    Act_Amount = Number of Activations
    Distribution = Amount of clusters that contain this group
    NGX = Node_Group X Cord (By default it's 0)
    NGY = Node_Group X Cord (By default it's 0)
    NGZ = Node_Group X Cord (By default it's 0)
    """
    
    group_name = models.CharField(max_length=20,verbose_name='Название Группы',primary_key=True)

    ngcl = models.ForeignKey(NGCL,related_name='Node_Group_Construct_List', on_delete=models.CASCADE, verbose_name="Конструкты Нод Группы")

    class StatusChoice(models.TextChoices):
        SOLID = 'solid', 'Цельная'
        BROKEN = 'broken', 'Сломанная'

    status = models.CharField(max_length = 6,verbose_name='статус',choices=StatusChoice.choices)
    act_amount = models.FloatField(verbose_name='Активации',default=1)
    distribution = models.FloatField(verbose_name='Распространенность',default=0)

    ngx = models.FloatField(verbose_name='X координата',default=0.0)
    ngy = models.FloatField(verbose_name='Y координата',default=0.0)
    ngz = models.FloatField(verbose_name='Z координата',default=0.0)

    

    ascension_date = models.DateTimeField(verbose_name="Дата Формирования", auto_now_add=True, null=True)
    last_activation = models.DateTimeField(verbose_name='Последняя Активация', auto_now_add=True,null=True)


    def __str__(self):
        return "NG - [%s] | Status - [%s] | NGX - [%s] | NGY - [%s] | NGZ - [%s]" % (self.group_name, self.status, self.ngx, self.ngy, self.ngz)

    class Meta:
        verbose_name_plural = 'Нод Группы'
        verbose_name = 'Нод Группа'
        ordering = ['last_activation']
