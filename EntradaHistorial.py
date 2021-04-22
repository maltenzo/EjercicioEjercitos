class EntradaHistorial():
    def __init__(self, numeroDeEjercitoEnemigo, nacionEnemiga):
        self.numeroDeEjercitoEnemigo = numeroDeEjercitoEnemigo
        self.nacionEnemiga = nacionEnemiga

    def actualizarSiGane(self, resultadoDeLaBatalla):
        self.resultadoDeLaBatalla = resultadoDeLaBatalla   