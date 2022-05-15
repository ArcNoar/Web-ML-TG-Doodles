from aiogram import types
from aiogram.dispatcher import FSMContext
from TG.loader import dp
import asyncio
from aiogram.dispatcher.filters import Text


from random import randint

import csv
import pandas as pd


from TG.states.Aspect_State import Aspect
from Functional.AspectF import SC_Random
from Functional.Prima_Func import Prima_sentence
from TG.sql.Prima_Mem import Prima_Categories, Prima_Contexts, VM_Correct_Answer, VM_InCorrect_Answer, VM_Trash_Answer

sent_template = Prima_sentence()


POS = False
NEG = False

Purpose_Find = True

actual_sentence = None # Актуальное предлоежние
US = None # Предложение пользователя
RS = None # Сгенерированное предложение

Category = 'Blank'
Cat_ID = '1'
Context = 'Zero'
Cont_ID = '1'

Grade_Dict = {}

Correction_Route = False
Fiction_Route = False

FUN_MODE = False


@dp.message_handler(commands="Aspect",state=None)
async def Aspect_Init(message: types.Message):
    global actual_sentence, FUN_MODE

    current_user = message.from_user
    Noah = 340981880
    Artur = 743865349

    

    #Word_func = VM_Word()
    #VM_Get = VM_Word.Get()
    #VM_Edit = VM_Word.Edit()

    #Alph_New = VM_Alph.New()

    if FUN_MODE == False:
        actual_sentence = None            
        if current_user.id == Noah:
        
            await Aspect.Initial.set()
            await message.answer('Нейрон Аспекта. Запуск.')
            await message.answer('Напишите что угодно.')
            
            #await dp.bot.send_message(current_user.id,'В общем. Ты перенаправлен в состояние инструктажа. \n Если ты уже проходил этот гайд, то напиши "Пропустить."')

        
        else:
            await message.answer('А ты уверен что у тебя есть права?')
    else:
        await Aspect.FunMode.set()
        await message.answer('Игровой режим? Ну ок, напиши что угодно,и я верну рандомное предложение.')

#Отмена.

@dp.message_handler(state='*', commands = 'закончили')
@dp.message_handler(Text(equals='закончили', ignore_case = True),state='*')
async def cancel_handler(message: types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ну окэ.')


@dp.message_handler(state=Aspect.FunMode)
async def Fun_Mode(message: types.Message,state: FSMContext):
    global actual_sentence, US , RS
    RS = SC_Random(Generated_Sentence=actual_sentence)
    actual_sentence = RS
    await message.answer(actual_sentence)
    actual_sentence = None
    await message.answer('Для повторной генерации снова напишите что угодно.')


@dp.message_handler(state=Aspect.Initial)
async def Listen_Answer(message: types.Message,state: FSMContext):
    global actual_sentence, US , RS , Purpose_Find
    US = (message.text).lower()
    print(f'-{US}')
    CA_Get = VM_Correct_Answer.Get()
    ICA_Get = VM_InCorrect_Answer.Get()

    potential_answer = CA_Get.sentence_data(US)
    #print(potential_answer)

    id_limiter = ICA_Get.max_id()
    if id_limiter == False:
        Purpose_Find = False
    else:
        pur_id = randint(1,id_limiter)
        purposed_answer = ICA_Get.by_id(pur_id)

    if potential_answer == False:
        if Purpose_Find == False:
            RS = SC_Random(Generated_Sentence=actual_sentence)
            actual_sentence = RS
            await message.answer(actual_sentence)
            print(f'-{actual_sentence}')
            await message.answer('Мой ответ корректный? (Да \ Нет)')

            await Aspect.Listen_Answer.set()
        else:
            actual_sentence = purposed_answer['AS']
            await message.answer(actual_sentence) 
            print(f'-{actual_sentence}')
            await message.answer('Это предложение имеет место быть здесь?')

            await Aspect.Pur_Find.set()

        

    else:
        if len(potential_answer) < 2:
            variate_answer = 0
            actual_sentence = potential_answer[variate_answer]['AS']
            await message.answer(actual_sentence)
            print(f'-{actual_sentence}')
            actual_sentence = None
        else:
            variate_answer = randint(0,len(potential_answer) - 1)
            actual_sentence = potential_answer[variate_answer]['AS']
            await message.answer(actual_sentence)
            print(f'-{actual_sentence}')
            actual_sentence = None

        

@dp.message_handler(state=Aspect.Pur_Find)
async def Grade_Init(message: types.Message,state: FSMContext):
    global Purpose_Find
    if (message.text).lower() == 'да':
        await message.answer('Хорошо. Но перенос предложения еще не предусмотрен, так что ничего не меняется. Возвращаю к первичному состоянию.')
        await message.answer('Напишите любое предложение')
        Purpose_Find = False
        actual_sentence = None
        await Aspect.Initial.set()
    elif (message.text).lower() == 'нет':
        await message.answer('Ну, оке, тогда действуем по рандому.')
        Purpose_Find = False
        actual_sentence = None
        await message.answer('Напишите любое предложение')
        await Aspect.Initial.set()
    else:
        await message.answer('Ой бля... я устала. Я пожалуй отдыхать.')

        await state.finish()

@dp.message_handler(state=Aspect.Listen_Answer)
async def Grade_Init(message: types.Message,state: FSMContext):
    global actual_sentence

    if (message.text).lower() == 'да':
        actual_sentence = RS
        await message.answer('Впишите ваши оценки. Всего 8 Оценок. ')
        await message.answer('G1[1-5] = Структура \n G2[1-5] = Грамматика \n G3[0-10] = Локальная Универсальность ')
        await message.answer('G4[0-10] = Глобальная Универсальность  \n G5[0-10] = МоноРезистентность \n G6[1-5] = Осмысленность ')
        await message.answer('G7[0-1] = Завершенность \n G8[0-1] = Гибкая Дополняемость')
         
        await Aspect.Pos_Grading.set()

        #actual_sentence = None
        
    elif (message.text).lower() == 'нет':
        #actual_sentence = None

        await message.answer('Мое предложение может быть использовано в качестве ответа на другое сообщение?')
        await Aspect.Neg_Nav.set()
        #await message.answer(f'Допускаете ли вы, что ваше предложение "{US}" \n Само по себе является некорректным? \n (Да \ Нет)')
        #await Aspect.Review.set()

    elif (message.text).lower() == 'заново':
        await message.answer('Ок. Напишите любое предложение.')
        await Aspect.Initial.set()



@dp.message_handler(state=Aspect.Neg_Nav)
async def Neg_Navigation(message: types.Message,state: FSMContext):
    global Fiction_Route, Correction_Route
    if (message.text).lower() == 'да':
        await message.answer('Хорошо, можете ли вы указать на какое сообщение это предложение отвечает?')
        Fiction_Route = True
        await Aspect.Neg_Route_Nav.set()

    elif (message.text).lower() == 'нет':
        
        await message.answer('Тогда желаете выполнить коррекцию моего предложения?')
        Correction_Route = True
        await Aspect.Neg_Route_Nav.set()
        

    else:
        await message.answer('Вы несоблюдаете формат ответа.')


@dp.message_handler(state=Aspect.Neg_Route_Nav)
async def Neg_Routing(message: types.Message,state: FSMContext):
    global Fiction_Route, Correction_Route
    if Fiction_Route == True:
        if (message.text).lower() == 'да':
            await message.answer('Хорошо, тогда напишите сообщение на которое мое предложение было бы ответом.')
            await Aspect.Fiction.set()
            Fiction_Route = False
        elif (message.text).lower() == 'нет':
            await message.answer('Ок, тогда перейдем к оценке качества моего предложения.')
            await Aspect.Neg_Grading.set()
            Fiction_Route = False

        else:
            await message.answer('Неправильный формат ответа.')
    elif Correction_Route == True:
        if (message.text).lower() == 'да':
            await message.answer('Хорошо, тогда напишите правильный ответ на ваше сообщение')
            await Aspect.Correction.set()
            Correction_Route = False
        elif (message.text).lower() == 'нет':
            await message.answer('Ок, тогда это предложение отправляется в мусор.')
            await Aspect.TRASH.set()
            Correction_Route = False

        else:
            await message.answer('Неправильный формат ответа.')

@dp.message_handler(state=Aspect.Fiction)
async def Fiction(message: types.Message,state: FSMContext):
    global US 
    US = (message.text).lower()

    await message.answer(f'\n -{US} \n -{actual_sentence}')
    await message.answer('Переходим в положительную ветку оценки.')
    await message.answer('Впишите ваши оценки. Всего 8 Оценок. ')
    await message.answer('G1[1-5] = Структура \n G2[1-5] = Грамматика \n G3[0-10] = Локальная Универсальность ')
    await message.answer('G4[0-10] = Глобальная Универсальность  \n G5[0-10] = МоноРезистентность \n G6[1-5] = Осмысленность ')
    await message.answer('G7[0-1] = Завершенность \n G8[0-1] = Гибкая Дополняемость')

    await Aspect.Pos_Grading.set()

@dp.message_handler(state=Aspect.Correction)
async def Correction(message: types.Message,state: FSMContext):
    global actual_sentence
    actual_sentence = (message.text).lower()

    await message.answer(f'\n -{US} \n -{actual_sentence}')
    await message.answer('Переходим в положительную ветку оценки.')
    await message.answer('Впишите ваши оценки. Всего 8 Оценок. ')
    await message.answer('G1[1-5] = Структура \n G2[1-5] = Грамматика \n G3[0-10] = Локальная Универсальность ')
    await message.answer('G4[0-10] = Глобальная Универсальность  \n G5[0-10] = МоноРезистентность \n G6[1-5] = Осмысленность ')
    await message.answer('G7[0-1] = Завершенность \n G8[0-1] = Гибкая Дополняемость')

    await Aspect.Pos_Grading.set()


@dp.message_handler(state=Aspect.Neg_Grading)
async def Neg_Grading(message: types.Message,state: FSMContext):
    global Grade_Dict, NEG

    NEG = True
    raw_grades = (message.text).split(' ')
    #print(raw_grades)

    cor_grades = []

    for i in raw_grades:
        
        # Определить что же такое F 
        try:
            
            if i == 'F':
                i = 1191033
                #print('FUCK')

            cor_grades.append(i)    
            #raw_grades[raw_grades.index(i_i)] = int(i_i)
            #print(type(raw_grades[raw_grades.index(i)]))

        except Exception as _ex:
            print('Это не числовая Оценка.',_ex)
    #print(cor_grades)
    Grade_Dict['1G'] = cor_grades[0]
    Grade_Dict['2G'] = cor_grades[1]
    Grade_Dict['3G'] = cor_grades[2]
    Grade_Dict['4G'] = cor_grades[3]
    Grade_Dict['5G'] = cor_grades[4]
    Grade_Dict['6G'] = cor_grades[5]
    Grade_Dict['7G'] = cor_grades[6]
    Grade_Dict['7.5G'] = cor_grades[7]

    if Grade_Dict['7G'] == 1:
        Grade_Dict['7G'] = True
    else:
        Grade_Dict['7G'] = False
    if Grade_Dict['7.5G'] == 1:
        Grade_Dict['7.5G'] = True
    else:
        Grade_Dict['7.5G'] = False
    
    

    try:
         await message.answer(f"""1G = {cor_grades[0]} \n 2G = {cor_grades[1]} \n 3G = {cor_grades[2]}
 4G = {cor_grades[3]} \n 5G = {cor_grades[4]}  \n 6G = {cor_grades[5]} \n 7G = {cor_grades[6]} \n 7.5G = {cor_grades[7]} """)
         await Aspect.ReCheck.set()
         await message.answer('Все верно? (Да\Нет)')

    except IndexError as _ex:
        await message.answer('Вы указали не все оценки.')



@dp.message_handler(state=Aspect.Pos_Grading)
async def Pos_Grading(message: types.Message,state: FSMContext):
    global Grade_Dict, POS
    
    POS = True
    raw_grades = (message.text).split(' ')
    #print(raw_grades)

    cor_grades = []

    for i in raw_grades:
        
        # Определить что же такое F 
        try:
            
            if i == 'F':
                i = 1191033
                #print('FUCK')

            cor_grades.append(i)    
            #raw_grades[raw_grades.index(i_i)] = int(i_i)
            #print(type(raw_grades[raw_grades.index(i)]))

        except Exception as _ex:
            print('Это не числовая Оценка.',_ex)
    #print(cor_grades)
    Grade_Dict['1G'] = cor_grades[0]
    Grade_Dict['2G'] = cor_grades[1]
    Grade_Dict['3G'] = cor_grades[2]
    Grade_Dict['4G'] = cor_grades[3]
    Grade_Dict['5G'] = cor_grades[4]
    Grade_Dict['6G'] = cor_grades[5]
    Grade_Dict['7G'] = cor_grades[6]
    Grade_Dict['7.5G'] = cor_grades[7]
    if Grade_Dict['7G'] == 1:
        Grade_Dict['7G'] = True
    else:
        Grade_Dict['7G'] = False
    if Grade_Dict['7.5G'] == 1:
        Grade_Dict['7.5G'] = True
    else:
        Grade_Dict['7.5G'] = False
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
         await message.answer(f"""1G = {cor_grades[0]} \n 2G = {cor_grades[1]} \n 3G = {cor_grades[2]}
 4G = {cor_grades[3]} \n 5G = {cor_grades[4]}  \n 6G = {cor_grades[5]} \n 7G = {cor_grades[6]} \n 7.5G = {cor_grades[7]} """)
         await Aspect.ReCheck.set()
         await message.answer('Все верно? (Да\Нет)')

    except IndexError as _ex:
        await message.answer('Вы указали не все оценки.')



@dp.message_handler(state=Aspect.TRASH)
async def Trash_Sent(message: types.Message,state: FSMContext):
    global actual_sentence
    Trash_Add = VM_Trash_Answer.New(actual_sentence)

    Trash_Add.sent_reg()

    await message.answer('Предложение занесено в мусор. Желаете продолжить?')
    actual_sentence = None
    # Add Repeat State 

    await Aspect.Repeating.set()




@dp.message_handler(state=Aspect.ReCheck)
async def Grade_Confirm(message: types.Message,state: FSMContext):
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
async def Cat_Set(message: types.Message,state: FSMContext):
    global Category, Cat_ID
    cat_name = (message.text).lower()
    if cat_name == 'f':
        cat_name = 'Нулевая'

    Cat_Get = Prima_Categories.Get()
    Cat_New = Prima_Categories.New()
    if Cat_Get.check_for(cat_name) == False:
        await message.answer(f'Создаем новую категорию : [{cat_name}]')
        Cat_New.category(cat_name)

    else:
        await message.answer(f'Такая категория уже сущесвует. "{US}" будет занесен в категорию [{cat_name}]')

    Category = cat_name

    Cat_ID = Cat_Get.get_id(Category)
    
    await message.answer(f'Категория : [{cat_name}] для "{US}"')
    
    await message.answer(f'Теперь введите контекст, если не уверены лучше поставьте F')

    await Aspect.Context_Set.set()


@dp.message_handler(state=Aspect.Context_Set)
async def Cont_Set(message: types.Message,state: FSMContext):
    global Context,Cont_ID

    cont_name = (message.text).lower()

    if cont_name == 'f':
        cont_name = 'Нулевой'


    Cont_Get = Prima_Contexts.Get()
    Cont_New = Prima_Contexts.New()
    if Cont_Get.check_for(cont_name) == False:
        await message.answer(f'Создаем новый контекст : [{cont_name}]')
        Cont_New.context(cont_name)

    else:
        await message.answer(f'Такой контекст уже сущесвует. "{US}" будет присвоен контекст [{cont_name}]')

    Context = cont_name

    Cont_ID = Cont_Get.get_id(Context)

    
    await message.answer(f'Для "{US}" : \n Ответ - {actual_sentence} \n Категория - {Category} \n Контекст - {Context}')


    await message.answer('Сохранить это предложение?')
    
    await Aspect.DB_Saving.set()

@dp.message_handler(state=Aspect.DB_Saving)
async def DB_Saver(message: types.Message,state: FSMContext):
    global POS,NEG, actual_sentence , sent_template

    if (message.text).lower() == 'да':
        if POS == True:
            sent_temp = sent_template.create()

            sent_temp['US'] = US
            sent_temp['AS'] = actual_sentence
            sent_temp['G1'] = Grade_Dict['1G']
            sent_temp['G2'] = Grade_Dict['2G']
            sent_temp['G3'] = Grade_Dict['3G']
            sent_temp['G4'] = Grade_Dict['4G']
            sent_temp['G5'] = Grade_Dict['5G']
            sent_temp['G6'] = Grade_Dict['6G']
            sent_temp['G7'] = Grade_Dict['7G']
            sent_temp['G8'] = Grade_Dict['7.5G']
            sent_temp['Категория'] = Cat_ID
            sent_temp['Контекст'] = Cont_ID

            Cor_Ans = VM_Correct_Answer.New(sent_temp)

            Cor_Ans.sent_reg()

            actual_sentence = None
            POS = False
            await message.answer('Начинаем заново?')
            await Aspect.Repeating.set()

        elif NEG == True:
            alt_temp = sent_template.alt_create()
            alt_temp['AS'] = actual_sentence
            alt_temp['G1'] = Grade_Dict['1G']
            alt_temp['G2'] = Grade_Dict['2G']
            alt_temp['G3'] = Grade_Dict['3G']
            alt_temp['G4'] = Grade_Dict['4G']
            alt_temp['G5'] = Grade_Dict['5G']
            alt_temp['G6'] = Grade_Dict['6G']
            alt_temp['G7'] = Grade_Dict['7G']
            alt_temp['G8'] = Grade_Dict['7.5G']
            alt_temp['Категория'] = Cat_ID
            alt_temp['Контекст'] = Cont_ID

            InCor_Ans = VM_InCorrect_Answer.New(sent_temp)

            InCor_Ans.sent_reg()
            actual_sentence = None
            NEG = False
            await message.answer('Начинаем заново?')
            await Aspect.Repeating.set()
      
    elif (message.text).lower() == 'нет':
        await message.answer('А? Какая то проблема? Ну тогда я стираю все данные этого предложения, даже спрашивать не буду что не так.')
        actual_sentence = None

        await message.answer('Начинаем заново?')
        await Aspect.Repeating.set()

    else:
        await message.answer('Мне правда нужно каждый раз говорить что ответ только Да или Нет?')


@dp.message_handler(state=Aspect.Repeating)
async def Repeat(message: types.Message,state: FSMContext):
    global Purpose_Find, actual_sentence
    if (message.text).lower() == 'да':
        await message.answer('Тогда впишите любое предложение.')
        Purpose_Find = True
        actual_sentence = None
        await Aspect.Initial.set()
      
    elif (message.text).lower() == 'нет':
        await message.answer('Ок. Выходим из состояния')
        await state.finish()

    else:
        await message.answer('Мне правда нужно каждый раз говорить что ответ только Да или Нет?')

    
    

"""
Во первых есть проблема того что мы находимся лишь на одной ветке одновременно.
Как бы ситуация когда предложение нормальное но мы идем по пути его коррекции потому что хотим задать ответ на сообщение это ыа
тип в идеале как то коррекцию и фикцию сделать параллельной

+ трабла в том, что у нас есть US - AS, и это хуево, потому что придется тогда задавать к каждому слову триллиард ответов?
Так щио у нас вариант такой
либо мы делаем сразу несколько проверок
где проверяем по тому совпадает ли оно, и проверяем по принадлежащей категории и таким образом пулим разные ответы.

ну и еще трабла в том что слишком строгое разделение на ответы и запросы.  Хотя в большинстве случаев стоит учесть и обратную схему.
Где ответ так же мог бы служить и запросом

+ такими темпами мы в контекстуалку скатимся

потому что мы слишком зависим от совпадений по слову.
Нужно больше сфокусироваться на оценке, но нам наверное нужно просто дробануть это все

По принципу "Мы точно знаем ответ" "Мы просто ведем логическую цепочку и предполагаем ответ"
как то так?
Хотя второй принцип это вообще тупняк


+ главная проблема это опять же слепота глобального диалога, она видит только одно сообщение, и нам надо это регулировать сука.

но каждый раз когда мы пишем сообщение он сука вызывает хендлер заново и потом как бы старое сообщение исчезает, что как бы писос.

Конечно я бы мог сделать стэйт сбора , а нет не мог, каким образом я 2 состояния сотворю? Значит нужно просто куда то логировать диалог.

Так тупо что я в итоге возвращаюсь к самой первой схеме и самому первому методу разговора.

___
Контексты потом надо разбить по оценка вроде, Дружеское / Вражбедное 
    Мягкое / Грубое 
    и тд.


Возможно и группировки слов надо параметризировать получше
но это по ходу дела.

А, еще стоит как то определять не по строгости, а по содержанию одного в другом, крч как контекстуальная нейронка
ДА ДА
КАКАЯ БЫ ОНА ТУПАЯ НЕ БЫЛА, ОНА ИМЕЕТ МЕСТО БЫТЬ


____
Таймлайн(Время Суток) тоже надо сделать, это пиздец как влияет на самом деле на форму ответа



"""





    


    
    