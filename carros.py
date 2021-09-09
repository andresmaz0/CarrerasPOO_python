'''
Por: Andres David Mazo Bossio
Fecha: 8/09/2021
Version: 1.0
'''

import random
datos=[]
ganadores=int(1)

class Juego:
    def __init__(self,n_carros,d_max):
        self.n_carros = n_carros
        self.distancia = d_max

class Carros(Juego):
    def __init__(self,list_car_name,nombre,carril,n_carros,d_max):
        super().__init__(n_carros,d_max)
        self.marca_carro = random.choice(list_car_name)
        self.n_carril = carril
        self.conductor = 'Es una maquina'
        self.nombre = nombre
        self.posicion = 0
        self.ganador = False

    def datos_de_jugadores(self):
        print('el {} {} que conduce un {}, esta en el carril N°{}'.format(self.nombre,self.conductor,self.marca_carro,
                                                                          self.n_carril))

    def datos_de_juego(self):
        print('el juego cuenta con {} competidroes y deben de recorrer una distancia de {} km'.format(self.n_carros,
                                                                                                      self.distancia))

#input
def crear_objs():
    num_carros = int(input('ingrese el numero de carros que van a competir: '))
    dis_max = int(input('ingrese la distancia en km que va a tener la pista: '))
    list_car_name=['Renault','Kia','Chevrolet','Mazda','Nissan','Toyota']
    for i in range(num_carros):
        player='player'+str(i+1)
        carril=int(i+1)
        competidor=Carros(list_car_name,player,carril,num_carros,dis_max)
        datos.append(competidor)

def modificador():
    estado=int(input('ingrese el numero de jugadores que van a ser conductores: '))
    if estado>0:
        for i in range(estado):
            datos[i].conductor = 'Es un jugador'
    else:
        print('todos los competidores son maquinas')
    for i in range(len(datos)):
        datos[i].datos_de_jugadores()

def carrera(ganadores):
    while ganadores!=4:
        for i in range(len(datos)):
            dado = random.randint(1, 6) * 100
            datos[i].posicion=datos[i].posicion+dado
            if datos[i].posicion>=(datos[i].distancia*1000) and datos[i].ganador==False:
                datos[i].ganador=True
                print('el puesto N° {} es para el {}'.format(ganadores,datos[i].nombre))
                ganadores=ganadores+1
            if ganadores==4:
                break

#main
crear_objs()
modificador()
carrera(ganadores)






