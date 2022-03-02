
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

