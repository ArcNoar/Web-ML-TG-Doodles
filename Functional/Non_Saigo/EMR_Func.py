
from datetime import date





class Emote_Temp:
    """
    Emote_Name = "MAIN_EMOTE - [?|?|?|?|?_?|?]" where ? = aspect_emote order by value

    Emote_Trigger(EMT) = user_id who causes the emotion (only if ET_Type = Creature, default = NULL)
    ET_Type = Creature/Ivent/Object/None (Type of EMT)
    ET_Descript = "Some note that describes EMT" , (if ET_type = Creature, can be NULL) *OPTIONAL*
    ET_Date = Sets_Automatically. str(data.today())

    Emote Components:
        FEAR (СТРАХ):
            Horror(Ужас)
            Anxiety(Тревога)
            Concern(Беспокойство)
            Astonishment(Удивление)
            Confusion(Замешательство)
            Timidity(Робость)
            Guilt(Вина)
            Embarrasment(Смущение)
            Doubt(Сомнение)
        ANGER (ГНЕВ):
            Rage(Ярость)
            Irritation(Раздражение)
            Resentment(Обида)
            Disgust(Отвращение)
            Jealousy(Ревность)
            Envy(Зависть)
            Indignation(Негодование)
            Nervousness(Нервозность)
            Disappointment(Разочарование)
        SORROW (ПЕЧАЛЬ):
            Idleness(Лень)
            Despait(Отчаяние)
            Compassion(Жалость)
            Loneliness(Отрешенность)
            Helpiness(Беспомощность)
            Aloofness(Отчужденность)
            Regret(Сожаление)
            Boredom(Скука)
            Sadness(Печаль)
        JOY (РАДОСТЬ):
            Happiness(Счастье)
            Delight(Восторг)
            Interest(Интерес)
            Excitement(Возбуждение)
            Curiosity(Любопытство)
            Confidence(Уверенность)
            Horny(Влечение)
            Laugh(Смех)
            Satisfaction(Удовлетворение)
    """
    def create(self):
        """
        Emote_Name = "MAIN_EMOTE - [?|?|?|?|? _ ?|?]" where ? = aspect_emote order by value
        """
        empty_emote = {
            'Код Эмоции' : 'SOMEEMOTE - [?|?|?|?|?_?|?]',
            'Сущность-Триггер' : None,
            'Тип Триггера' : 'None',
            'Описание' : 'Нулевое Описание',
            'Дата' : str(date.today()),
            'Эмоция': {
                'СТРАХ' : {
                    'Ужас' : 0.0,
                    'Тревога' : 0.0,
                    'Беспокойство' : 0.0,
                    'Удивление' : 0.0,
                    'Замешательство' : 0.0,
                    'Робость' : 0.0,
                    'Вина' : 0.0,
                    'Смущение' : 0.0,
                    'Сомнение' : 0.0,
                    },

                'ГНЕВ' : {
                    'Ярость' : 0.0,
                    'Раздражение' : 0.0,
                    'Обида' : 0.0,
                    'Отвращение' : 0.0,
                    'Ревность' : 0.0,
                    'Зависть' : 0.0,
                    'Негодование' : 0.0,
                    'Нервозность' : 0.0,
                    'Разочарование' : 0.0,
                    },

                'ГРУСТЬ' : {
                    'Лень' : 0.0,
                    'Отчаяние' : 0.0,
                    'Жалость' : 0.0,
                    'Отрешенность' : 0.0,
                    'Беспомощность' : 0.0,
                    'Отчужденность' : 0.0,
                    'Сожаление' : 0.0,
                    'Скука' : 0.0,
                    'Печаль' : 0.0,
                    },

                'РАДОСТЬ' : {
                    'Счастье' : 0.0,
                    'Восторг' : 0.0,
                    'Интерес' : 0.0,
                    'Возбуждение' : 0.0,
                    'Любопытство' : 0.0,
                    'Уверенность' : 0.0,
                    'Хорни' : 0.0,
                    'Смех' : 0.0,
                    'Удовлетворение' : 0.0,
                    },
                },
            }
        return empty_emote

def ETD_single(emote_list): 
    """
    ETD = Conver To Dict
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    

    """
    data_list = emote_list
    try:
        converted_data = {
                'ID' : data_list[0][0],
                'Код Эмоции' : data_list[0][1],
                'Сущность-Триггер' : data_list[0][41],
                'Тип Триггера' : data_list[0][2],
                'Описание' : data_list[0][3],
                'Дата' : str(data_list[0][4]),
                'Эмоция': {
                    'СТРАХ' : {
                        'Ужас' : data_list[0][5],
                        'Тревога' : data_list[0][6],
                        'Беспокойство' : data_list[0][7],
                        'Удивление' : data_list[0][8],
                        'Замешательство' : data_list[0][9],
                        'Робость' : data_list[0][10],
                        'Вина' : data_list[0][11],
                        'Смущение' : data_list[0][12],
                        'Сомнение' : data_list[0][13],
                        },

                    'ГНЕВ' : {
                        'Ярость' : data_list[0][14],
                        'Раздражение' : data_list[0][15],
                        'Обида' : data_list[0][16],
                        'Отвращение' : data_list[0][17],
                        'Ревность' : data_list[0][18],
                        'Зависть' : data_list[0][19],
                        'Негодование' : data_list[0][20],
                        'Нервозность' : data_list[0][21],
                        'Разочарование' : data_list[0][22],
                        },

                    'ГРУСТЬ' : {
                        'Лень' : data_list[0][23],
                        'Отчаяние' : data_list[0][24],
                        'Жалость' : data_list[0][25],
                        'Отрешенность' : data_list[0][26],
                        'Беспомощность' : data_list[0][27],
                        'Отчужденность' : data_list[0][28],
                        'Сожаление' : data_list[0][29],
                        'Скука' : data_list[0][30],
                        'Печаль' : data_list[0][31],
                        },

                    'РАДОСТЬ' : {
                        'Счастье' : data_list[0][32],
                        'Восторг' : data_list[0][33],
                        'Интерес' : data_list[0][34],
                        'Возбуждение' : data_list[0][35],
                        'Любопытство' : data_list[0][36],
                        'Уверенность' : data_list[0][37],
                        'Хорни' : data_list[0][38],
                        'Смех' : data_list[0][39],
                        'Удовлетворение' : data_list[0][40],
                        },
                    },
                }
        
        return converted_data
    except Exception as _ex:
        print(_ex)


def ETD_many(emote_list):
    """
    !!! ONLY FOR CONVERT SQL REQUEST DATA_LIST !!!
    ETD = Conver To Dict
    data_list = Pm_sql(user_data).get_user() => returns [(ID,first_name,sur_name,....,appearance)]
    # Это можно по сути сделать основной функцией пушо что один что много, норм буит
    """
    dt_list = emote_list
    collected_emotions = []
    for data_list in dt_list:
        
        try:
            converted_data = {
                'ID' : data_list[0],
                'Код Эмоции' : data_list[1],
                'Сущность-Триггер' : data_list[41],
                'Тип Триггера' : data_list[2],
                'Описание' : data_list[3],
                'Дата' : str(data_list[4]),
                'Эмоция': {
                    'СТРАХ' : {
                        'Ужас' : data_list[5],
                        'Тревога' : data_list[6],
                        'Беспокойство' : data_list[7],
                        'Удивление' : data_list[8],
                        'Замешательство' : data_list[9],
                        'Робость' : data_list[10],
                        'Вина' : data_list[11],
                        'Смущение' : data_list[12],
                        'Сомнение' : data_list[13],
                        },

                    'ГНЕВ' : {
                        'Ярость' : data_list[14],
                        'Раздражение' : data_list[15],
                        'Обида' : data_list[16],
                        'Отвращение' : data_list[17],
                        'Ревность' : data_list[18],
                        'Зависть' : data_list[19],
                        'Негодование' : data_list[20],
                        'Нервозность' : data_list[21],
                        'Разочарование' : data_list[22],
                        },

                    'ГРУСТЬ' : {
                        'Лень' : data_list[23],
                        'Отчаяние' : data_list[24],
                        'Жалость' : data_list[25],
                        'Отрешенность' : data_list[26],
                        'Беспомощность' : data_list[27],
                        'Отчужденность' : data_list[28],
                        'Сожаление' : data_list[29],
                        'Скука' : data_list[30],
                        'Печаль' : data_list[31],
                        },

                    'РАДОСТЬ' : {
                        'Счастье' : data_list[32],
                        'Восторг' : data_list[33],
                        'Интерес' : data_list[34],
                        'Возбуждение' : data_list[35],
                        'Любопытство' : data_list[36],
                        'Уверенность' : data_list[37],
                        'Хорни' : data_list[38],
                        'Смех' : data_list[39],
                        'Удовлетворение' : data_list[40],
                        },
                    },
                }
            
            collected_emotions.append(converted_data)
        except Exception as _ex:
            print(_ex)
    return collected_emotions