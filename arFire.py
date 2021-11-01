import numpy as np
import random
from arFront import *

def retornar_random_percent(min_num=0, max_num=100):
    return random.randint(min_num,max_num)/100

def retorn_cor_fire(percent):
    return (int(255*percent),int(140*percent),int(10*percent))

class Fire:
    def __init__(self, tamanho=[20,2]):
        self.tamanho = tamanho
        self.fire_array = np.zeros(tamanho)
        self.min_num_fire = 40
    
    def update(self):
        self.fire_array[0] = retornar_random_percent(75)
        shape = self.fire_array.shape
        
        for i in random.sample(range(shape[1]), k=int(shape[1]*0.25)):
            coluna = self.fire_array[:,i]
            for y in random.sample(range(1, shape[0]), k=int(shape[0]*0.2)):
                coluna[y] = coluna[y-1] * retornar_random_percent(min_num=self.min_num_fire)

        return self.fire_array
    

if __name__ == '__main__':
    fire1 = Fire([15,70])
    win = App(tema=universeCodeTheme, nomeJanela='arFire')
    win.txFps.active = True

    lbInten_fire = win.novoTexto(lugar=[0.415, 0.675])

    lbTitulo = win.novoTexto(
        lugar=[0.39,0.1],
        tamanho=25,
        string='Algoritmo arFire'
    )

    def put_mais_fogo():
        new_val = int(fire1.min_num_fire+1)
        if new_val > 70: new_val = 70
        fire1.min_num_fire = new_val

    btMaisfogo = win.novoBotao(
        string='Mais fogo',
        lugar=[0.525, 0.61],
        command=put_mais_fogo,
        bordas=2,
        cor=win.cor_back
    )

    def put_menos_fogo():
        new_val = int(fire1.min_num_fire-1)
        if new_val < 10: new_val = 10
        fire1.min_num_fire = new_val

    btMenosfogo = win.novoBotao(
        string='Menos fogo',
        lugar=[0.375, 0.61],
        command=put_menos_fogo,
        bordas=2,
        cor=win.cor_back
    )

    fr1 = win.novoSquare([0.35, 0.6], tamanho=[0.3, 0.125])

    running = True
    while running:

        porc_fire = (fire1.min_num_fire-10)/60
        porc_fire_format =  str(int(porc_fire*100)) + '%'

        lbInten_fire.string = f'Intensidade do fogo: {porc_fire_format}'

        win_exit = win.update()
        data_fire = fire1.update()

        for i in range(fire1.tamanho[1]):
            
            coluna = fire1.fire_array[:,i]
            for y in range(0, fire1.tamanho[0]):
                cel_percent = coluna[y]
                cor_sq = retorn_cor_fire(cel_percent)
                tamanho_sq = [7, 8]
                pos_inicial = [150, 300]
                lugar_sq = [pos_inicial[0]+((tamanho_sq[0])*i), pos_inicial[1]-(tamanho_sq[1]*y)]

                win.drawSquare(cor=cor_sq, lugar=lugar_sq, tamanho=tamanho_sq, radius=1)

        if win_exit == 'finish': running = False
