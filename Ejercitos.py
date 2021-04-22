from random import randint
#------------------------------------Comentarios-----------------------------------------#
# Considero que el codigo esta escrito de forma autocomentada, es decir que se puede ver que pasa aun si no hubiera comentarios
# Aun asi deje comentarios por las dudas de que se espere que el codigo este comentado
#



#-------------------------------Naciones-----------------------------------------------#
class Nacion():
    #-------------------------Generadores-----------------------------------------------#
    def __init__(self):
       self.ejercitos = []
       self.crearEjercito()

    #crea un ejercito y lo añade al arreglo de la nacion
    def crearEjercito(self):
        pass

    #batalla mi ejercito con otro (podria ser de la misma nacion)    
    def batallarMiEjercitoContraElDe(self, miNumeroDeEjercito, numeroDeEjercitoEnemigo, nacionEnemiga):
        self.ejercitos[miNumeroDeEjercito].batallarContra(nacionEnemiga.ejercitos[numeroDeEjercitoEnemigo])
    
    #entrena una unidad en un ejercito especifico, cada unidad se encarga de saber como entrenar
    def entrenarIesimaUnidadDelJesimoEjercito(self, indiceDeUnidad, indiceDeEjercito):
        self.miJesimoEjercito(indiceDeEjercito).entrenarIesimaUnidad(indiceDeUnidad)

    #transforma una unidad en un ejercito especifico, cada unidad se encarga de saber como transformarse
    def transformarIesimaUnidadDelJesimoEjercito(self, indiceDeUnidad, indiceDeEjercito):
        self.miJesimoEjercito(indiceDeEjercito).transformarIesimaUnidad(indiceDeUnidad) 



    #--------------------------------- observadores para tests ----------------------------#

    #devuelve el jesimo ejercito de mi arreglo de ejercitos
    def miJesimoEjercito(self, indiceDeEjercito):
        return self.ejercitos[indiceDeEjercito]

    #devuelve el oro del jesimo ejercito de mi arreglo de ejercitos
    def verOroDeMiJesimoEjercito(self, indiceDeEjercito):
        return self.ejercitos[indiceDeEjercito].verOroDelEjercito()

    #devuelve la fuerza de la iesima unidad del jesimo ejercito de mi arreglo de ejercitos
    def verFuerzaDeLaIesimaUnidadDelJesimoEjercito(self, indiceDeUnidad, indiceDeEjercito):
         return self.miJesimoEjercito(indiceDeEjercito).verFuerzaDeLaIesimaUnidad(indiceDeUnidad)

    #devuelve la clase de la iesima unidad del jesimo ejercito de mi arreglo de ejercitos
    def verClaseDeLaIesimaUnidadDelJesimoEjercito(self, indiceDeUnidad, indiceDeEjercito):
        return self.miJesimoEjercito(indiceDeEjercito).verClaseDeLaIesimaUnidad(indiceDeUnidad)

    #devuelve un booleano diciendo si de la iesima unidad del jesimo ejercito de mi arreglo de ejercitos esta eliminada
    def verEstadoEliminadoDeLaIesimaUnidadDlJesimoEjercito(self, indiceDeUnidad, indiceDeEjercito):
        return self.miJesimoEjercito(indiceDeEjercito).verEstadoEliminadoDeLaIesimaUnidad(indiceDeUnidad)

    #devuelve la cantidad de unidades del jesimo ejercito de mi arreglo de ejercitos
    def cantidadDeUnidadesEliminadasDelJesimoEjercito(self, indiceDeEjercito):
        return self.miJesimoEjercito(indiceDeEjercito).cantidadDeUnidadesEliminadas()    


class NacionChina(Nacion):
    def crearEjercito(self):
        self.ejercitos.append(EjercitoChino())

    
class NacionInglesa(Nacion):
     def crearEjercito(self):
        self.ejercitos.append(EjercitoIngles())


class NacionBizantina(Nacion):
     def crearEjercito(self):
        self.ejercitos.append(EjercitoBizantino())






#-----------------------------Ejercitos------------------------------------------------#
class Ejercito():
    #----------------------------Generadores--------------------------------------#
    def __init__(self):
        self.oro = 1000
        self.unidades = self.crearUnidades() 

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

    #avisa el ejercito que perdio 
    def perdi(self):
        self.eliminarDosUnidadesDeMayorPuntaje()

    #avisa el ejercito que empato 
    def empate(self):
        self.eliminarUnidadRandom()  

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
    #devuelve los puntos de fuerza actual de la unidad
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



