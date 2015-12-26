#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import unittest
from modules import trx


class TestTrx(unittest.TestCase):

    """docstring for TestTrx"""

    def test_TestRunData(self):
        path_archivo = "/home/matibarriento/Downloads/TestResultFailed.trx"
        trx_module = trx
        resultado = trx_module.ObtenerDatos(path_archivo)
        propiedades = ["id_testrun",
                       "nombre_maquina_testrun",
                       "nombre_usuario_testrun",
                       "creacion_testrun",
                       "finalizacion_testrun",
                       "encolado_testrun",
                       "inicio_testrun",
                       "duracion_testrun",
                       "id_configuraciones",
                       "nombre_configuraciones",
                       "deployado",
                       "resultado",
                       "abortados",
                       "completos",
                       "desconectados",
                       "errores",
                       "ejecutados",
                       "fallidos",
                       "en_progreso",
                       "inconclusos",
                       "no_ejecutados",
                       "no_ejecutables",
                       "pasados",
                       "pasados_abortados",
                       "pendientes",
                       "timeout",
                       "total",
                       "alertas"]
        for prop in propiedades:
            self.assertIn(prop, resultado.__dict__, "{0} no existe".format(prop))
            self.assertIsNotNone(resultado.__dict__[prop], "{0} es None".format(prop))
        self.assertGreater(len(resultado.tests), 0, "No hay tests")
        self.assertGreater(len(resultado.listas_test), 0, "No hay listas")
        self.assertGreater(len(resultado.clases_test), 0, "No hay clases")

    def test_UnittestData(self):
        path_archivo = "/home/matibarriento/Downloads/TestResultFailed.trx"
        trx_module = trx
        resultado = trx_module.ObtenerDatos(path_archivo)
        self.assertGreater(len(resultado.tests), 0, "No hay test")
        test = resultado.tests[0]
        propiedades = [
                        "id",
                        "computadora_test",
                        "duracion",
                        "fin",
                        "id_ejecucion",
                        "resultado",
                        "resultado_id",
                        "inicio",
                        "id_lista",
                        "nombre_test",
                        "tipo_test",
                        "clase_test",
                        ]
        for prop in propiedades:
            self.assertIn(prop, test.__dict__, "{0} no existe".format(prop))
            self.assertIsNotNone(test.__dict__[prop], "{0} es None".format(prop))

    def test_ListaData(self):
        path_archivo = "/home/matibarriento/Downloads/TestResultFailed.trx"
        trx_module = trx
        resultado = trx_module.ObtenerDatos(path_archivo)
        self.assertGreater(len(resultado.listas_test), 0, "No hay listas")
        lista = resultado.listas_test[0]
        propiedades = [
                        "id_lista",
                        "nombre_lista",
                        "tests",
                        "exitosos",
                        "exitoso",
                        "duracion"
                        ]
        for prop in propiedades:
            self.assertIn(prop, lista.__dict__, "{0} no existe".format(prop))
            self.assertIsNotNone(lista.__dict__[prop], "{0} es None".format(prop))

        self.assertGreater(len(lista.tests), 0, "No hay tests")

    def test_ClaseData(self):
        path_archivo = "/home/matibarriento/Downloads/TestResultFailed.trx"
        trx_module = trx
        resultado = trx_module.ObtenerDatos(path_archivo)
        self.assertGreater(len(resultado.listas_test), 0, "No hay listas")
        clase = resultado.clases_test[0]
        propiedades = [
                        "nombre_clase",
                        "tests",
                        "exitosos",
                        "exitoso",
                        "duracion"
                        ]
        for prop in propiedades:
            self.assertIn(prop, clase.__dict__, "{0} no existe".format(prop))
            self.assertIsNotNone(clase.__dict__[prop], "{0} es None".format(prop))

        self.assertGreater(len(clase.tests), 0, "No hay tests")


if __name__ == '__main__':
    unittest.main()
