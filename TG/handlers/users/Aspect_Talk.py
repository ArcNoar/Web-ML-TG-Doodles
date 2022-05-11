from aiogram import types
from aiogram.dispatcher import FSMContext
from TG.loader import dp
import asyncio
from aiogram.dispatcher.filters import Text




import csv
import pandas as pd


from TG.states.Aspect_State import Aspect
from Functional.AspectF import SC_Random
from TG.sql.Prima_Mem import Prima_Categories, Prima_Contexts


actual_sentence = None # Актуальное предлоежние
US = None # Предложение пользователя
RS = None # Сгенерированное предложение

Category = 'Blank'
Context = 'Zero'

Grade_Dict = {}



@dp.message_handler(commands="Aspect",state=None)
async def Aspect_Init(message: types.Message):
    global actual_sentence

    current_user = message.from_user
    Noah = 340981880
    Artur = 743865349

    

    #Word_func = VM_Word()
    #VM_Get = VM_Word.Get()
    #VM_Edit = VM_Word.Edit()

    #Alph_New = VM_Alph.New()

    
    actual_sentence = None            
    if current_user.id == Noah:
    
        await Aspect.Initial.set()
        await message.answer('Нейрон Аспекта. Запуск.')
        await message.answer('Напишите что угодно.')
        
        #await dp.bot.send_message(current_user.id,'В общем. Ты перенаправлен в состояние инструктажа. \n Если ты уже проходил этот гайд, то напиши "Пропустить."')

    
    else:
        await message.answer('А ты уверен что у тебя есть права?')

#Отмена.

@dp.message_handler(state='*', commands = 'закончили')
@dp.message_handler(Text(equals='закончили', ignore_case = True),state='*')
async def cancel_handler(message: types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ну окэ.')



@dp.message_handler(state=Aspect.Initial)
async def Listen_Answer(message: types.Message,state: FSMContext):
    global actual_sentence, US , RS
    US = message.text

    RS = SC_Random(Generated_Sentence=actual_sentence)
    actual_sentence = RS

    await message.answer(actual_sentence)

    await message.answer('Мой ответ корректный? (Да \ Нет)')

    await Aspect.Listen_Answer.set()

@dp.message_handler(state=Aspect.Listen_Answer)
async def Grading(message: types.Message,state: FSMContext):
    global actual_sentence

    if (message.text).lower() == 'да':
        actual_sentence = RS
        await message.answer("""
            Напишите 3 оценки в формате : ОЦЕНКА ОЦЕНКА ОЦЕНКА ... 
            (каждая оценка разделяется пробелом)

            -Если сомневаетесь или не можете дать конкретную оценку напишите F

            -Иногда отсутствие оценки лучше чем недостоверная оценка.

            -Рассматривайте каждую! оценку независимо от другой,
            (3,4,5) могут показаться схожими, но важно чтобы вы рассматривали каждый! вопрос независимо)

            - За исключение (7,7.5)
            """)

        await message.answer("""
            
                1 Оценка [1 - 5] - Насколько хороша постановка и конструкция? 

            2 Оценка [1 - 5] - Насколько хороша грамматическая составляющая и окончания? 

            3 Оценка [0 - 10] - Насколько универсален мой ответ в рамках контекста вашего предложения? 

            4 Оценка [0 - 10] - Насколько универсален мой ответ в рамках нескольких (Любых) контекстов? 

            5 Оценка [0 - 10] - Насколько мой ответ устойчив к его *повторяемости* ? 
            *(Если я буду часто его использовать, станет ли его уместность хуже?)*

            6 Оценка [1 - 5] - Насколько мой ответ соответсвует *смыслу* вашего предложения? 
            *(Подразумевается вариант где вам понравился мой ответ, но в общем смысле это высказывание не совсем в тему.)*
                       
            7 Оценка [0 - 1] - Считаете ли вы мой ответ завершенным в его *конструкции*? 
            *(Является оно полным и самостоятельным, или имеет место быть другим словам?)*

            7.5 Оценка [0 - 1] - Дополнение должно быть строгим или в большинстве случаев дополнение этого предложения, не испортит его? 
        """)
        
        await Aspect.Pos_Grading.set()

        actual_sentence = None
        
    elif (message.text).lower() == 'нет':
        actual_sentence = None
        await message.answer(f'Допускаете ли вы, что ваше предложение "{US}" \n Само по себе является некорректным? \n (Да \ Нет)')
        await Aspect.Review.set()


@dp.message_handler(state=Aspect.Review)
async def Grading(message: types.Message,state: FSMContext):
    if (message.text).lower() == 'да':
        await message.answer('Ну и хули тогда ты от меня хочешь?')
        await state.finish()
        actual_sentence = None
    elif (message.text).lower() == 'нет':
        # Уточнение назначения слова.
        await message.answer('Хорошо. Тогда на данном этапе все.')
        await state.finish()
        actual_sentence = None

    else:
        await message.answer('Вы несоблюдаете формат ответа.')



@dp.message_handler(state=Aspect.Pos_Grading)
async def Grading(message: types.Message,state: FSMContext):
    global Grade_Dict
    
    raw_grades = (message.text).split(' ')
    #print(raw_grades)
    for i in raw_grades:
        # Добавить счетчик недостояющих значений (F)
        # Определить что же такое F
        try:
            raw_grades[raw_grades.index(i)] = int(i)
            #print(type(raw_grades[raw_grades.index(i)]))

        except Exception as _ex:
            print('Это не числовая Оценка.',_ex)
    #print(raw_grades)
    Grade_Dict['1G'] = raw_grades[0]
    Grade_Dict['2G'] = raw_grades[1]
    Grade_Dict['3G'] = raw_grades[2]
    Grade_Dict['4G'] = raw_grades[3]
    Grade_Dict['5G'] = raw_grades[4]
    Grade_Dict['6G'] = raw_grades[5]
    Grade_Dict['7G'] = raw_grades[6]
    Grade_Dict['7.5G'] = raw_grades[7]
    """
    Тут переход в некст состояние, в котором мы переспрашиваем насчет корректности оценок.
    Потом переходим в состояние где устанавливаем контекст если пользователь конечно может его установить.
    И потом заносим в цсв
    Надо будет еще проверку совпадений по этим контекстам сделать
    а то получится песос
    
    Ну а по негативным оценкам там вообще иная обработка и иной ЦСВ
    Мы там скорее убеждаемся или смотрим НАСКОЛЬКО оно плохо
    И мб просим вариант того как нам стоило бы ответить.

    """


    try:
         await message.answer(f"""1G = {raw_grades[0]} \n 2G = {raw_grades[1]} \n 3G = {raw_grades[2]}
 4G = {raw_grades[3]} \n 5G = {raw_grades[4]}  \n 6G = {raw_grades[5]} \n 7G = {raw_grades[6]} \n 7.5G = {raw_grades[7]} """)
         await Aspect.ReCheck.set()
         await message.answer('Все верно? (Да\Нет)')

    except IndexError as _ex:
        await message.answer('Вы указали не все оценки.')


@dp.message_handler(state=Aspect.ReCheck)
async def Grading(message: types.Message,state: FSMContext):
    if (message.text).lower() == 'да':
        await message.answer('Хорошо. Тогда переходим к установке Категории.')
        await Aspect.Cat_Set.set()
        await message.answer(f'Напишите название для категории к которой принадлежит "{US}", если не знаете , напишите F')
        
    elif (message.text).lower() == 'нет':
        # Уточнение назначения слова.
        await message.answer(f'Тогда напишите свои оценки снова. Оцениваемое предложение : "{US}"')
        await Aspect.Pos_Grading.set()
        

    else:
        await message.answer('Вы несоблюдаете формат ответа.')


@dp.message_handler(state=Aspect.Cat_Set)
async def Grading(message: types.Message,state: FSMContext):
    global Category
    cat_name = (message.text).lower()
    if cat_name = 'f':
        cat_name = 'Нулевая'

    Cat_Get = Prima_Categories.Get()
    Cat_New = Prima_Categories.New()
    if Cat_Get.check_for(cat_name) == False:
        await message.answer(f'Создаем новую категорию : [{cat_name}]')
        Cat_New.category(cat_name)

    else:
        await message.answer(f'Такая категория уже сущесвует. "{US}" будет занесен в категорию [{cat_name}]')

    Category = cat_name
    
    await message.answer(f'Категория : [{cat_name}] для "{US}"')
    
    await message.answer(f'Теперь введите контекст, если не уверены лучше поставьте F')

    await Aspect.Context_Set.set()


@dp.message_handler(state=Aspect.Context_Set)
async def Grading(message: types.Message,state: FSMContext):
    global Context

    cont_name = (message.text).lower()

    if cont_name = 'f':
        cont_name = 'Нулевой'


    Cont_Get = Prima_Contexts.Get()
    Cont_New = Prima_Contexts.New()
    if Cont_Get.check_for(cont_name) == False:
        await message.answer(f'Создаем новый контекст : [{cont_name}]')
        Cont_New.context(cont_name)

    else:
        await message.answer(f'Такой контекст уже сущесвует. "{US}" будет присвоен контекст [{cont_name}]')

    Context = cont_name
    
    await message.answer(f'Контекст : [{cont_name}] для "{US}"')
    
    






    


    
    