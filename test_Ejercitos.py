import unittest
import Naciones as Ejercicio
from Unidades import Piquero
from Unidades import Arquero
from Unidades import Caballero

#-------------------------------------------Comentarios------------------------------------------#
# Para testear unidades voy a usar, en general, al ejercito ingles porque tiene una distribucion simple de las tropas:
# 0 - 9 piqueros, 10 - 19 arqueros, 20 - 29 caballeros

COSTE_ENTRENAMIENTO_PIQUERO = 10
COSTE_ENTRENAMIENTO_ARQUERO = 20
COSTE_ENTRENAMIENTO_CABALLERO = 30

COSTE_TRANSFORMACION_PIQUERO_ARQUERO = 30
COSTE_TRANSFORMACION_ARQUERO_CABALLERO = 40

DIFERENCIA_DE_ATAQUE_BASE_ENTRE_PIQUERO_Y_ARQUERO = 5
ATAQUE_QUE_GANA_AL_ENTRENAR_UN_PIQUERO = 3
ATAQUE_QUE_GANA_AL_ENTRENAR_UN_ARQUERO = 7
ATAQUE_QUE_GANA_AL_ENTRENAR_UN_CABALLERO = 10

ORO_IMICIAL = 1000
ORO_POR_VICTORIA = 100

class TestsBasicos(unittest.TestCase):
    def setUp(self):
        #--------------Naciones--------------------#
        self.nacionChina = Ejercicio.NacionChina()
        self.nacionInglesa = Ejercicio.NacionInglesa()
        self.nacionBizantina = Ejercicio.NacionBizantina()

        #------------Unidades De Referencia--------#    
        self.piqueroDeReferencia = Piquero()
        self.arqueroDeReferencia = Arquero()
        self.caballeroDeReferencia = Caballero()
        
    def test_todas_las_Naciones_inician_con_1000_de_oro_en_sus_ejercitos(self):
        self.assertEqual(ORO_IMICIAL, self.nacionChina.verOroDeMiJesimoEjercito(0))
        self.assertEqual(ORO_IMICIAL, self.nacionInglesa.verOroDeMiJesimoEjercito(0))
        self.assertEqual(ORO_IMICIAL, self.nacionInglesa.verOroDeMiJesimoEjercito(0))

   
    def test_entrenar_piquero_aumenta_su_fuerza_en_3_y_saca_10_de_oro_al_ejercito(self):
        self.nacionInglesa.entrenarIesimaUnidadDelJesimoEjercito(0,0)
        self.assertEqual(self.piqueroDeReferencia.fuerzaActual() + ATAQUE_QUE_GANA_AL_ENTRENAR_UN_PIQUERO, self.nacionInglesa.verFuerzaDeLaIesimaUnidadDelJesimoEjercito(0,0))
        self.assertEqual(ORO_IMICIAL - COSTE_ENTRENAMIENTO_PIQUERO , self.nacionInglesa.verOroDeMiJesimoEjercito(0)) 

    def test_entrenar_arquero_aumenta_su_fuerza_en_7_y_saca_20_de_oro_al_ejercito(self):
        self.nacionInglesa.entrenarIesimaUnidadDelJesimoEjercito(10,0)
        self.assertEqual(self.arqueroDeReferencia.fuerzaActual() + ATAQUE_QUE_GANA_AL_ENTRENAR_UN_ARQUERO, self.nacionInglesa.verFuerzaDeLaIesimaUnidadDelJesimoEjercito(10,0))
        self.assertEqual(ORO_IMICIAL - COSTE_ENTRENAMIENTO_ARQUERO, self.nacionInglesa.verOroDeMiJesimoEjercito(0)) 

    def test_entrenar_caballero_aumenta_su_fuerza_en_10_y_saca_30_de_oro_al_ejercito(self):
        self.nacionInglesa.entrenarIesimaUnidadDelJesimoEjercito(20,0)
        self.assertEqual(self.caballeroDeReferencia.fuerzaActual() + ATAQUE_QUE_GANA_AL_ENTRENAR_UN_CABALLERO, self.nacionInglesa.verFuerzaDeLaIesimaUnidadDelJesimoEjercito(20,0))
        self.assertEqual(ORO_IMICIAL - COSTE_ENTRENAMIENTO_CABALLERO, self.nacionInglesa.verOroDeMiJesimoEjercito(0))         

    def test_transformar_piquero_en_arquero_cambia_la_clase_aumenta_el_ataque_y_descuenta_30_de_oro_al_ejercito(self):
        self.nacionInglesa.transformarIesimaUnidadDelJesimoEjercito(0,0)
        self.assertEqual(self.arqueroDeReferencia.__class__, self.nacionInglesa.verClaseDeLaIesimaUnidadDelJesimoEjercito(0,0))
        self.assertEqual(self.arqueroDeReferencia.fuerzaActual(), self.nacionInglesa.verFuerzaDeLaIesimaUnidadDelJesimoEjercito(0,0))
        self.assertEqual(ORO_IMICIAL - COSTE_TRANSFORMACION_PIQUERO_ARQUERO , self.nacionInglesa.verOroDeMiJesimoEjercito(0)) 

    def test_transformar_arquero_en_caballero_cambia_la_clase_aumenta_el_ataque_y_descuenta_40_de_oro_al_ejercito(self):
        self.nacionInglesa.transformarIesimaUnidadDelJesimoEjercito(10,0)
        self.assertEqual(self.caballeroDeReferencia.fuerzaActual(), self.nacionInglesa.verFuerzaDeLaIesimaUnidadDelJesimoEjercito(10,0))
        self.assertEqual(self.caballeroDeReferencia.__class__, self.nacionInglesa.verClaseDeLaIesimaUnidadDelJesimoEjercito(10,0))
        self.assertEqual(ORO_IMICIAL - COSTE_TRANSFORMACION_ARQUERO_CABALLERO, self.nacionInglesa.verOroDeMiJesimoEjercito(0))     

    def test_transformar_caballero_no_reduce_el_oro_ni_cambia_la_clase(self):
        self.nacionInglesa.transformarIesimaUnidadDelJesimoEjercito(20,0)
        self.assertEqual(self.caballeroDeReferencia.__class__, self.nacionInglesa.verClaseDeLaIesimaUnidadDelJesimoEjercito(20,0))
        self.assertEqual(ORO_IMICIAL, self.nacionInglesa.verOroDeMiJesimoEjercito(0))  

    def test_transformar_unidades_no_descarta_los_puntos_que_ganaron_entrenando_previamente(self):
        self.nacionInglesa.entrenarIesimaUnidadDelJesimoEjercito(0,0)
        ataqueAntesDeTransformarse = self.nacionInglesa.verFuerzaDeLaIesimaUnidadDelJesimoEjercito(0,0)
        self.nacionInglesa.transformarIesimaUnidadDelJesimoEjercito(0,0)
        self.assertEqual(ataqueAntesDeTransformarse + DIFERENCIA_DE_ATAQUE_BASE_ENTRE_PIQUERO_Y_ARQUERO, self.nacionInglesa.verFuerzaDeLaIesimaUnidadDelJesimoEjercito(0,0))

    def test_al_ganar_una_batalla_el_ejercito_ganador_obtiene_100_de_oro(self):
        self.nacionBizantina.batallarMiEjercitoContraElDe(0, 0, self.nacionChina)
        self.assertEqual(ORO_IMICIAL + ORO_POR_VICTORIA, self.nacionBizantina.verOroDeMiJesimoEjercito(0))

    def test_al_perder_una_batalla_el_ejercito_perdedor_pierde_sus_dos_unidades_de_mayor_fuerza(self):
        self.nacionBizantina.batallarMiEjercitoContraElDe(0, 0, self.nacionChina)
        self.assertNotEqual(self.caballeroDeReferencia.estoyEliminado(), self.nacionChina.verEstadoEliminadoDeLaIesimaUnidadDlJesimoEjercito(28, 0))
        self.assertNotEqual(self.caballeroDeReferencia.estoyEliminado(), self.nacionChina.verEstadoEliminadoDeLaIesimaUnidadDlJesimoEjercito(27, 0))

    def test_al_empatar_se_pierde_una_unidad_aleatoria(self):
        self.nacionBizantina.crearEjercito()
        self.nacionBizantina.batallarMiEjercitoContraElDe(0, 1, self.nacionBizantina)
        self.assertEqual(1, self.nacionBizantina.cantidadDeUnidadesEliminadasDelJesimoEjercito(0))
        self.assertEqual(1, self.nacionBizantina.cantidadDeUnidadesEliminadasDelJesimoEjercito(1))

    def test_al_tener_una_batalla_los_ejercitos_y_empatan_actualizan_sus_historiales_de_forma_correcta(self):
        self.nacionBizantina.crearEjercito()
        self.nacionBizantina.batallarMiEjercitoContraElDe(0, 1, self.nacionBizantina)

        self.assertEqual("Empate", self.nacionBizantina.miJesimoEjercito(0).historial[-1].resultadoDeLaBatalla)
        self.assertEqual("Empate", self.nacionBizantina.miJesimoEjercito(1).historial[-1].resultadoDeLaBatalla)

        self.assertEqual(self.nacionBizantina, self.nacionBizantina.miJesimoEjercito(0).historial[-1].nacionEnemiga)
        self.assertEqual(self.nacionBizantina, self.nacionBizantina.miJesimoEjercito(1).historial[-1].nacionEnemiga)

        self.assertEqual(1, self.nacionBizantina.miJesimoEjercito(0).historial[-1].numeroDeEjercitoEnemigo)
        self.assertEqual(0, self.nacionBizantina.miJesimoEjercito(1).historial[-1].numeroDeEjercitoEnemigo)

    def test_al_tener_una_batalla_los_ejercitos_actualizan_sus_historiales_de_forma_correcta(self):
        self.nacionChina.crearEjercito()
        self.nacionBizantina.batallarMiEjercitoContraElDe(0, 1, self.nacionChina)

        self.assertEqual("Gane", self.nacionBizantina.miJesimoEjercito(0).historial[-1].resultadoDeLaBatalla)
        self.assertEqual("Perdi", self.nacionChina.miJesimoEjercito(1).historial[-1].resultadoDeLaBatalla)

        self.assertEqual(self.nacionChina, self.nacionBizantina.miJesimoEjercito(0).historial[-1].nacionEnemiga)
        self.assertEqual(self.nacionBizantina, self.nacionChina.miJesimoEjercito(1).historial[-1].nacionEnemiga)

        self.assertEqual(1, self.nacionBizantina.miJesimoEjercito(0).historial[-1].numeroDeEjercitoEnemigo)
        self.assertEqual(0, self.nacionChina.miJesimoEjercito(1).historial[-1].numeroDeEjercitoEnemigo)    