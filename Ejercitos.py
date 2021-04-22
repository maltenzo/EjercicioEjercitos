from random import randint
from EntradaHistorial import EntradaHistorial
from Unidades import Piquero
from Unidades import Arquero
from Unidades import Caballero





#-----------------------------Ejercitos------------------------------------------------#
class Ejercito():
    #----------------------------Generadores--------------------------------------#
    def __init__(self):
        self.oro = 1000
        self.unidades = self.crearUnidades() 
        self.historial = []

    #crea las unidades basicas del ejercito, cada ejercito de las naciones sabe como responder este mensaje
    def crearUnidades(self):
        pass
    
    #crea la cantidad de unidades de piqueros, arqueros, caballeros de acuerdo a lo que se indica por los parametros
    def crearUnidadesDePiquerosArquerosCaballeros(self, cantidadPiqueros, cantidadArqueros, cantidadCaballeros):
        piqueros = self.crearNUnidadesDe(Piquero(), cantidadPiqueros)
        arqueros = self.crearNUnidadesDe(Arquero(), cantidadArqueros)
        caballeros = self.crearNUnidadesDe(Caballero(), cantidadCaballeros)
        return piqueros + arqueros + caballeros

    #batalla este ejercito contra el especificado por parametro
    def batallarContra(self, otroEjercito):
        if otroEjercito != self:
            if self.fuerzaDelEjercito() > otroEjercito.fuerzaDelEjercito():
                self.gane()
                otroEjercito.perdi()
            elif self.fuerzaDelEjercito() > otroEjercito.fuerzaDelEjercito():
                self.perdi()
                otroEjercito.gane()
            else:
                self.empate()
                otroEjercito.empate()            
        
    #crea N unidades del tipo de unidad especificada por parametros
    def crearNUnidadesDe(self, tipoDeUnidad, cantidadDeUnidades):
        unidad = tipoDeUnidad.__class__
        listaDeUnidades = [unidad() for i in range(0, cantidadDeUnidades)]
        return listaDeUnidades
    
    def registrarBatallaEnHistorial(self, numeroDeEjercitoEnemigo, nacionEnemiga):
        nuevaEntrada = EntradaHistorial(numeroDeEjercitoEnemigo, nacionEnemiga)
        self.historial.append(nuevaEntrada)

    def actualizarHistorialDeBatalla(self, resultadoDeLaBatalla):
        self.historial[-1].actualizarSiGane(resultadoDeLaBatalla)

    #entrena a la iesima unidad del arreglo de unidades, cada unidad sabe como responder el mensaje entrenar
    def entrenarIesimaUnidad(self, indice):
        self.entrenarUnidad(self.unidades[indice])

    #le avisa a la unidad especificada por parametro que entrene
    def entrenarUnidad(self, unidad):
        if not unidad.estoyEliminado() and self.oro >= unidad.verCostoPorEntrenar():
            self.oro -= unidad.verCostoPorEntrenar()
            unidad.entrenar()    

    #transforma a la iesima unidad del arreglo de unidades, cada unidad sabe como responder el mensaje entrenar
    def transformarIesimaUnidad(self, indice):
        unidadTransformada = self.transformarUnidad(self.unidades[indice])    
        self.unidades[indice]=unidadTransformada

    #le avisa a la unidad especificada por parametro que entrene para transfomrarse
    def transformarUnidad(self, unidad):
        if not unidad.estoyEliminado() and self.oro >= unidad.verCostoPorTransformacion():
            self.oro -= unidad.verCostoPorTransformacion()
            unidadTransformada = unidad.transformar()      
            return unidadTransformada

    #elimina la unidad de mayor puntaje de ataque de este ejercito
    def eliminarUnidadDeMayorPuntaje(self):
        unidadDeMayorPuntaje = self.buscarUnidadDeMayorPuntaje()
        self.eliminarUnidad(unidadDeMayorPuntaje)  

    #elimina las dos unidades de mayor puntaje de ataque de este ejercito
    def eliminarDosUnidadesDeMayorPuntaje(self):
        self.eliminarUnidadDeMayorPuntaje() 
        self.eliminarUnidadDeMayorPuntaje()
    
    #devuelve la unidad de mayor puntaje
    def buscarUnidadDeMayorPuntaje(self):
        unidadDeMayorPuntaje = None
        for unidad in self.unidades:
            if unidadDeMayorPuntaje == None or unidadDeMayorPuntaje.fuerzaActual() < unidad.fuerzaActual():
                unidadDeMayorPuntaje = unidad
        return unidadDeMayorPuntaje   

    #le avisa a la unidad especificada por parametro que esta eliminada
    def eliminarUnidad(self, unidad):
        if unidad != None:
            unidad.eliminar() 

    #avisa el ejercito que ganó 
    def gane(self):
        self.oro += 100
        self.actualizarHistorialDeBatalla("Gane")

    #avisa el ejercito que perdio 
    def perdi(self):
        self.eliminarDosUnidadesDeMayorPuntaje()
        self.actualizarHistorialDeBatalla("Perdi")

    #avisa el ejercito que empato 
    def empate(self):
        self.eliminarUnidadRandom()
        self.actualizarHistorialDeBatalla("Empate")  

    #elimina una unidad al azar (podria pasar que trate de eliminar uno que ya esta eliminado, me parece una mecanica interesante  para jugar con la suerte asi que lo dejo asi)
    def eliminarUnidadRandom(self):
        unidadRandom = self.unidades[randint(0, len(self.unidades))]
        self.eliminarUnidad(unidadRandom)

    #--------------------------------Observadores------------------------------------------#
    #devuelve la puntuacion total de fuerza del ejercito
    def fuerzaDelEjercito(self):
        fuerzaDelEjercito = 0
        for unidad in self.unidades:
            fuerzaDelEjercito += unidad.fuerzaActual()
        return fuerzaDelEjercito

    #--------------------------------Observadores para tests--------------------------------#
    
    # devuelve el oro del ejercito
    def verOroDelEjercito(self):
        return self.oro        

    #devuelve los puntos de fuerza de la iesima unidad del arreglo de unidades
    def verFuerzaDeLaIesimaUnidad(self, indiceDeUnidad):
        return self.unidades[indiceDeUnidad].fuerzaActual()

    #devuelve la clase de la iesima unidad del arreglo de unidades
    def verClaseDeLaIesimaUnidad(self, indiceDeUnidad):
        return self.unidades[indiceDeUnidad].__class__
    
    
    #devuelve un booleano que dice si la iesima unidad del arreglo de unidades esta eliminada
    def verEstadoEliminadoDeLaIesimaUnidad(self, indiceDeUnidad):
        return self.unidades[indiceDeUnidad].estoyEliminado()

    #devuelve la cantidad de unidades eliminadas en este ejercito
    def cantidadDeUnidadesEliminadas(self):
        cantidadDeUnidadesEliminadas = 0
        for unidad in self.unidades:
            if unidad.estoyEliminado():
                cantidadDeUnidadesEliminadas+=1
        return cantidadDeUnidadesEliminadas        


class EjercitoChino(Ejercito):
    

    def crearUnidades(self):
        return self.crearUnidadesDePiquerosArquerosCaballeros(2, 25, 2)

    
class EjercitoIngles(Ejercito):
   

    def crearUnidades(self):

         return self.crearUnidadesDePiquerosArquerosCaballeros(10, 10, 10)
    

class EjercitoBizantino(Ejercito):

    
     def crearUnidades(self):
        return self.crearUnidadesDePiquerosArquerosCaballeros(5, 8, 15)



