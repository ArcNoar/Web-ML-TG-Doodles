from random import randint
import numpy as np

"""
# G3/4 Pm 1/4 L3

Dima = ((((0.75 * (0.75 / (2/4)))) + ((0.75 * (0.25 / (2/4))))) + (((0.25 / (0.75 / (2/4)))) + ((0.25 * (0.25 / (2/4)))))) * 10



Masha = ((((0.5 * (0.75 / (3/4)))) + ((0.5 * (0.25 / (3/4))))) + (((0.5 / (0.5 / (3/4)))) + ((0.5 * (0.75 / (3/4)))))) * 10

D_battle_point = round((Dima * 10),2)

M_battle_point = round((Masha * 10),2)

print(f'Dima Score : {D_battle_point}')

print(f'Masha Score : {M_battle_point}')
"""
"""
our_money = 150000000

dpercent = 0.13

def year_profit(money,percent):
    
    start_money = money
    print(f'Start Capital : {start_money} \n')
    current_money = money
    month_profit = 0
    pass_month = 0

    while month_profit < 600000:
        pass_month += 1
        month_profit = ((current_money * 30) / 360) * percent

        current_money += month_profit


    print(f'Pass Month : {pass_month}')
    print(f'Profit Summary : {current_money - start_money}')
    print(f'Final Capital : {current_money}')
    
year_profit(our_money,dpercent)

#print(f'Our money  {our_money}  |  profit : {((our_money * 30) / 360) * dpercent}')
"""


def get_grade(s1,s2,s3):
    m_grade = np.mean([s1,s2,s3])

    if m_grade < 90:
        
        if m_grade < 80:
            if m_grade < 70:
                if m_grade < 60:
                        return "F"
                else:
                    return "D"
            else:
                return "C"
        else:
            return "B"
    else:
        return "A"

def get_grade(s1,s2,s3):
    m_grade = np.mean([s1,s2,s3])

    if m_grade >= 90:
        return "A"

    elif m_grade >= 80:
        return "B"
    elif m_grade >= 70:
        return "C"
    elif m_grade >= 60:
        return "D"
    else:
        return "F"
   


        