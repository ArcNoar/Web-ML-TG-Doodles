from aiogram import types
from aiogram.dispatcher import FSMContext
from TG.loader import dp




from Functional.Prima_Func import Prima_sentence, Prima_word, parse , G_Delay

from TG.sql.Prima_Mem import VM_Alph, VM_Word , VM_Sentence


word_template = Prima_word() # Темплейт запоминания слов
word_params = word_template.create()

sent_template = Prima_sentence() # Темплейт для запоминания предложения
sent_config = sent_template.create()



@dp.message_handler(state=None)
async def word_remember(message: types.Message):
    

    current_user = message.from_user
    Noah = 340981880
    Artur = 743865349

    

    Word_func = VM_Word()
    VM_Get = VM_Word.Get()
    #VM_Edit = VM_Word.Edit()

    Alph_New = VM_Alph.New()

    
                
    if current_user.id == Noah:
    
        if message.text == 'Я состоятельный' :
    
            await message.answer('К сожалению я не могу определить вашего состояния')
        elif (message.text).startswith('Напиши Артуру :') == True:
                    response = (message.text)[15:]
                    print(response)
                    await dp.bot.send_message(743865349, f"{response}")
                    await dp.bot.send_message(Noah, f"{response}")
        
            
    
        else:
            
            await message.answer('Ыа. Не понимаю твоего сблева.')
            """
            try:
    
                sentence = message.text
    
                words = sentence.split(' ')
    
                for word in words:
                    
                    for letter in word:
                        #print(letter)
                        Alph_New.add_construct(letter.lower())
                        
    
                await message.answer('Хм...')
    
            except Exception as _ex:
                pass
                #print('Blyat',_ex)
            
             
            """
            """
            try:
                
                lines = (message.text).splitlines()
                bag_of_word = []

                for line in lines:
                    for w in line.split():
                        except_symbol = ['.','?',',','(',')','!',"'",'"','*'] # Вернуть дефис

                        word = [i for i in w if i not in except_symbol]
                        #symbols = [i for i in w if i in except_symbol]
                        word = ''.join(word)
                        
                        bag_of_word.append(word)
                print(bag_of_word)
                for word in bag_of_word:
                    if word == '':
                        word = 'пустота'
                    else:
                        #print(word)
                        word = word.lower()
                        #print(normal_word)
                        word_params['Слово'] = word
                        #word_params['Тип'] = G_Delay(parse(word))
                        #print(word_params['Тип'])
                        word_params['Тип'] = 'PTICK'
                        #print(word_params)
                        
                        #print(word)
                        Word_add = Word_func.New(word_params)
                        Word_add.learn_word()
                #await message.answer('Оке...')
            except Exception as _ex:
                print('Запоминание слов пошло пиздй братанчик.',_ex)
            """
            """
            try:
  
                
                sent_config['Предложение'] = (message.text).lower()
                #sent_config['От кого'] = current_user.id
                Sentence_Func = VM_Sentence.New(sent_config)
                Sentence_Func.sent_reg()
            except Exception as _ex: 
                print('Регистрация предложения провалилась. Ну или просто коряво прошла. Я хз ес чесна.',_ex)
            """ 
    
            """
            try:
                
                sentence_lenght = randint(2,10)
    
                sentence_parts = []
                sent = ''
                exception_counter = 0
                limiter = 0
                while limiter < sentence_lenght:
                    try:
                        max_ID = VM_Get.max_id()
                        word_ident = str(randint(1,int(max_ID['ID'])))
                        pulled_word = VM_Get.word_by_id(word_ident)
                        sentence_parts.append(pulled_word['Слово'])
                        limiter += 1
                    except Exception as _ex:
                        #print('ОШИБКА БРАТАН. СЕНТЕНС КОНСТРУКТОР ХУЙНЯ',_ex)
                        if exception_counter < 10:
                            continue
                        else:
                            break
    
                sent = ' '.join(sentence_parts)
                await message.answer(sent)
            except Exception as _ex:
                print('При попытке спиздануть что то, возникла ошибка',_ex)
            """
                    
     
    else:
        await dp.bot.send_message(Noah, f"{message.text}")
    