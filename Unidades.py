

#------------------------------Unidades-----------------------------------------------#
class Unidad():
     #----------------------------Generadores--------------------------------------#
    def __init__(self):
        pass

    #actualiza la fuerza de la unidad con el nuevo valor pasado por parametro
    def setearFuerza(self, nuevosPuntosDeFuerza):
        self.puntosDeFuerza = nuevosPuntosDeFuerza    

    #aumenta la fuerza de la unidad en el valor pasado por parametro
    def aumentarFuerzaEn(self, puntosDeFuerzaExtra):
         self.setearFuerza(self.fuerzaActual() + puntosDeFuerzaExtra)

    #entrena la unidad, cada subclase sabe como responder este mensaje
    def entrenar(self):
        pass

    #marca la unidad como eliminada
    def eliminar(self):
        self.eliminado = True    

    #transforma el soldad, cada subclase sabe como responder este mensaje
    def transformarSoldado(self):
        pass    

    #--------------------------------Observadores----------------------------------#
    #devuelve los puntos de fuerza actual de la unidad, si la unidad esta eliminada devuelve 0
    def fuerzaActual(self):
        puntosDeFuerzaDeLaUnidad = 0
        if not self.eliminado:
            puntosDeFuerzaDeLaUnidad = self.puntosDeFuerza
        return puntosDeFuerzaDeLaUnidad     
    
    #devuelve el costo del entrenamiento de la unidad
    def verCostoPorEntrenar(self):
        return self.costoDeEntrenamiento

    #devuelve el coste del entrenamiento para transformarse en otra unidad
    def verCostoPorTransformacion(self):
        return self.costoDeTransformacion

    #devuelve el booleano que representa si la unidad esta eliminada
    def estoyEliminado(self):
        return self.eliminado    

   
class Piquero(Unidad):
    #----------------------------Generadores--------------------------------------#
    def __init__(self):
        self.puntosDeFuerza = 5
        self.costoDeEntrenamiento = 10
        self.costoDeTransformacion = 30
        self.eliminado = False


    def entrenar(self):
        puntosObtenidosPorEntrenamiento = 3
        self.aumentarFuerzaEn(puntosObtenidosPorEntrenamiento) 


    def transformar(self):
        diferenciaDeFuerzaEntreArqueroYPiquero = 5
        nuevoArquero = Arquero()
        nuevoArquero.setearFuerza(self.fuerzaActual() + diferenciaDeFuerzaEntreArqueroYPiquero)
        return nuevoArquero


class Arquero(Unidad):
    #----------------------------Generadores--------------------------------------#
    def __init__(self):
        self.puntosDeFuerza = 10
        self.costoDeEntrenamiento = 20
        self.costoDeTransformacion = 40
        self.eliminado = False


    def entrenar(self):
        puntosObtenidosPorEntrenamiento = 7
        self.aumentarFuerzaEn(puntosObtenidosPorEntrenamiento)    


    def transformar(self):
        diferenciaDeFuerzaEntreCaballeroYArquero = 10
        nuevoCaballero = Caballero()
        nuevoCaballero.setearFuerza(self.fuerzaActual() + diferenciaDeFuerzaEntreCaballeroYArquero)
        return nuevoCaballero    


class Caballero(Unidad):
    #----------------------------Generadores--------------------------------------#
    def __init__(self):
        self.puntosDeFuerza = 20
        self.costoDeEntrenamiento = 30
        self.costoDeTransformacion = 0
        self.eliminado = False


    def entrenar(self):
       puntosObtenidosPorEntrenamiento = 10
       self.aumentarFuerzaEn(puntosObtenidosPorEntrenamiento)  


    def transformar(self):
        return self    



