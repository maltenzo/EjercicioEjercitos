from Ejercitos import EjercitoChino
from Ejercitos import EjercitoIngles
from Ejercitos import EjercitoBizantino
#------------------------------------Comentarios-----------------------------------------#
# Considero que el codigo esta escrito de forma autocomentada, es decir que se puede ver que pasa aun si no hubiera comentarios
# Aun asi deje comentarios por las dudas de que se espere que el codigo este comentado


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




