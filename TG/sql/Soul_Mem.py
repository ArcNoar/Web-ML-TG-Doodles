import psycopg2

from .conf import db_name,host,user,password


"""
Identity
Like_Dislike
Motives
postulates
Emote_Reg
"""


class Emote_Reg:
    def Em_Code_Create(self,em_dict):
        """
        ���������� ������ = '-Domin_Name-|Code|Code|Code -Sup_Name-|Code|Code|Code'
        """

       
        Code_Ref = {
            '�����' : {
                'Hrr' : '����',
                'Anx' : '�������',
                'Crn' : '������������',
                'Ast' : '���������',
                'Cnf' : '��������������', 
                'Tmd' : '�������',
                'Glt' : '����', 
                'Emb' : '��������', 
                'Dbt' : '��������'
            },
            '����' : {
                'Rge' : '������', 
                'Irr' : '�����������', 
                'Rsn' : '�����',
                'Dgt' : '����������', 
                'Jls' : '��������', 
                'Env' : '�������',
                'Idn' : '�����������', 
                'Nrs' : '�����������', 
                'Dsp' : '�������������'
            },
            '������' : {
                'Idl' : '����',
                'Dst' : '��������',
                'Cmp' : '�������',
                'Lns' : '������������',
                'Hls' : '�������������',
                'Afs' : '�������������',
                'Rgt' : '���������',
                'Bdm' : '�����',
                'Sdn' : '������'
            },
            '�������' : {
                'Hps' : '�������',
                'Dlt' : '�������',
                'Ist' : '�������',
                'Ext' : '�����������',
                'Cty' : '�����������',
                'Cfd' : '�����������',
                'Hrn' : '��������',
                'Lgh' : '����',
                'Stf' : '��������������'
            }
        }
    
        Sum_Of_aspects = {}
        sorted_sum_aspects = []
    
        def get_key(d, value):
            for k, v in d.items():
                if v == value:
                    return k
    
        # �������� ������������ ������ � ������������� ����� ��������� ��� ������.
        for emote in em_dict:
            em_value = sum(em_dict[f"{emote}"].values())
            em_value = f'{em_value:.1f}'
            #print(f' ���� ������ -  {emote} : {em_value} \n' + ('-' * 10))
            Sum_Of_aspects[f'{emote}'] = float(em_value)
    
        sorted_sum_aspects = sorted((list(Sum_Of_aspects.values())))
        sorted_sum_aspects.reverse() # ��������� � �������� ��� ��������
    
        Domin_Emote = get_key(Sum_Of_aspects,max(sorted_sum_aspects))
        Sup_Emote = get_key(Sum_Of_aspects,sorted_sum_aspects[1])
    
        DE_dict = em_dict[f'{Domin_Emote}']
        SE_dict = em_dict[f'{Sup_Emote}']
        
        def Code_construct(domin_list,sup_list): # ������������ ��� ������
            DE_list = sorted(list(domin_list.values()))
            DE_list.reverse()
            SE_list = sorted(list(sup_list.values()))
            SE_list.reverse()
            
            def NM_Create(some_list,some_dict): # �������� �������������� ������ �������� ������
                Value_list = []
                Name_List = []
                for aspect in some_list:
                    if aspect < 0.5:
                        #print('������� ������ - ���������� ����')
                        break
                    else:
                        Value_list.append(aspect)
                for value in Value_list:
                    Name_List.append(get_key(some_dict,value))
    
                return Name_List
    
            Domin_NL = NM_Create(DE_list,DE_dict)
            Sup_NL = NM_Create(SE_list,SE_dict)
            Sum_NL = Domin_NL + Sup_NL
            
            """
            
            ��� ����� � ������ �������� �� �����������.
            """
            def Code_Creating(name_list,Dom_Em,Sup_Em): # ������������ � ���������� ��������� � ������ ��� ������
                Code_List = []
                Emote_Code = f'-{Dom_Em}-|'
                #print(name_list)
                #print(Code_Ref[f'{Dom_Em}'])
                for aspect_name in name_list:
                    #print(aspect_name)
                    key = get_key(Code_Ref[f'{Dom_Em}'],aspect_name)
                    if key != None:
                        Code_List.append(key)
                Code_List.append(f' -{Sup_Em}-')
                for aspect_name in name_list:
                    key = get_key(Code_Ref[f'{Sup_Em}'],aspect_name)
                    if key != None:
                        Code_List.append(key)
                
                #print(Code_List)   
                Emote_Code = Emote_Code + '|'.join(Code_List)
                return Emote_Code
            return Code_Creating(Sum_NL,Domin_Emote,Sup_Emote)
        
        return Code_construct(DE_dict,SE_dict)
        



    
    class New:
        def __init__(self,em_data):
            self.Emote_Components = em_data['������']
            code_func = Emote_Reg()
            self.Em_Code = code_func.Em_Code_Create(self.Emote_Components)
    class Get:
        pass


    class Edit:
        """
        �� ���� ������������� � ����.
        """
        pass
    class Del:
        """
        �� ���� ������������� � ����.
        """
        pass
    

