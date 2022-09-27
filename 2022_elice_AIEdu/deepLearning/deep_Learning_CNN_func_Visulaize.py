import matplotlib.pyplot as plt

def Visulaize(histories,key='loss'):
    for name,history in histories:
        plt.plot(history.epoch,history.history[key],
                 label=name.title()+'Train')
    plt.xlabel('Epochs')
    plt.ylabel(key.replace('_',' ').title())
    plt.legend()
    plt.xlim([0,max(history.epoch)])