




word = 'Блять...'

"""
def w_filter(w):
    except_symbol = ['.','?',',','(',')','!',"'",'"','-']

    word = [i for i in w if i not in except_symbol]
    word = ''.join(word)
    print(word)

    #print(set(word) - set(except_symbol))

#w_filter(word)

"""
#delayer_left = 0
#delayer_right = 1

#print(word[delayer_left:delayer_right])


listed = [0,1,2,3,4]
word_list = [i for i in word]
wl = word_list.copy()
for i in word_list:
    print(i)
    popped = wl.pop(wl.index(i))
    print(popped)