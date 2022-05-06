


def alpha_trainer(model):
    lr = 0.00001
    best_ccp = 0.00625
    current_ccp = 0.00001
    best_acc = 1.3
    num_epoches = 1000
    


    for epoche in range(num_epoches):
        
        model_acc = model(word=None,ccpa=current_ccp)
        if model_acc <= best_acc:
            current_ccp += lr
        else:
            best_ccp = current_ccp
            best_acc = model_acc

        if (epoche + 1) % 100 == 0:
            print(f'epoch {epoche + 1}/{num_epoches}, cur_alpha = {current_ccp} , best_alpha = {best_ccp}, Best_Acc = {best_acc}')
    print("_-_" * 10)        

    return best_ccp

"""
def R_Finder(model):
    lr = 1
    best_r = 1
    current_r = 1
    best_acc = 1.3
    num_epoches = 100
    


    for epoche in range(num_epoches):
        
        model_acc = model(word=None,ccpa=current_ccp)
        if model_acc <= best_acc:
            current_r += lr
        else:
            best_r = current_r
            best_acc = model_acc

        if (epoche + 1) % 100 == 0:
            print(f'epoch {epoche + 1}/{num_epoches}, cur_alpha = {current_r} , best_r = {best_r}, Best_Acc = {best_acc}')
    print("_-_" * 10)        

    return best_r

"""