from sklearn.ensemble import GradientBoostingClassifier
import numpy as np

from AI_Gen.Data_Prep.MB_Data_Prep import GX_Base # General Grad X

# Grad Y for each Type
from AI_Gen.Data_Prep.MB_Data_Prep import GY_Verb

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Noun

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Name

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Ptick

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Union

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Prepos

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Nomin

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Adjective

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Inter

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Deprich

from AI_Gen.Data_Prep.MB_Data_Prep import GY_State

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Numin

from AI_Gen.Data_Prep.MB_Data_Prep import GY_Prich


def Verb_Gmodel(word):
    print('Мы в глаголе.')
    
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Verb)
    
    return model.predict(word)

def Noun_Gmodel(word):
    print('Мы в Существительном.')
    model = GradientBoostingClassifier()
    GX = np.array(GX_Base)
    print(GX)
    model.fit(GX, np.array(GY_Noun))
    
    return model.predict(word)

def Name_Gmodel(word):
    print('Мы в имени.')
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Name)
    
    return model.predict(word)

def Ptick_Gmodel(word):
    print('Мы в частице.')
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Ptick)
    
    return model.predict(word)

def Union_Gmodel(word):
    
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Union)
    
    return model.predict(word)

def Prepos_Gmodel(word):
    print('Мы в препосе.')
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Prepos)
    
    return model.predict(word)

def Nomin_Gmodel(word):
    print('Мы в Номине.')
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Nomin)
    
    return model.predict(word)

def Adjective_Gmodel(word):
    print('Мы в прилагательном.')
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Adjective)
    
    return model.predict(word)

def Inter_Gmodel(word):
    print('Мы в Интере.')
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Inter)
    
    return model.predict(word)

def Deprich_Gmodel(word):
    print('Мы в деепричастии.')
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Deprich)
    
    return model.predict(word)

def State_Gmodel(word):
    print('Мы в наречии.')
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_State)
    
    return model.predict(word)

def Numin_Gmodel(word):
    print('Мы в Числительном.')
    model = GradientBoostingClassifier()
    GX = np.array(GX_Base)
    model.fit(GX, GY_Numin)
    
    return model.predict(word)

def Prich_Gmodel(word):
    print('Мы в причастии.')
    model = GradientBoostingClassifier()
    model.fit(GX_Base, GY_Prich)
    
    return model.predict(word)


Gmodel_list = {
                'Verb' : Verb_Gmodel,
                'Noun' : Noun_Gmodel,
                'Name' : Name_Gmodel,
                'Ptick' : Ptick_Gmodel,
                'Union' : Union_Gmodel,
                'Prepos' : Prepos_Gmodel,
                'Nomin' : Nomin_Gmodel,
                'Adjective' : Adjective_Gmodel,
                'Inter' : Inter_Gmodel,
                'Deprich' : Deprich_Gmodel,
                'State' : State_Gmodel,
                'Numin' : Numin_Gmodel,
                'Prich' : Prich_Gmodel,
               }