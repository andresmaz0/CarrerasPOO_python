class Persona:
    pass
    def __init__(self,peso,altura):
        self.peso = peso
        self.altura = altura

    def comentario(self,nombre):
        return '{} pesa {} kg y mide {} cm '.format(nombre,self.peso,self.altura)

persona1 = Persona(75,1.78)
print(persona1.comentario('maria'))