#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function
import unittest
from modules import trx


class TestTrx(unittest.TestCase):

    """docstring for TestTrx"""

    def test_TestRunData(self):

        path_archivo = "/home/matibarriento/Downloads/TestResultFailed.trx"
        trx_module = trx
        resultado = trx_module.ObtenerDatos(path_archivo).__dict__
        for method in [self.assertIsNotNone, self.assertIn]:
            method("id_testrun", resultado)
            method("nombre_maquina_testrun", resultado)
            method("nombre_usuario_testrun", resultado)
            method("creacion_testrun", resultado)
            method("finalizacion_testrun", resultado)
            method("encolado_testrun", resultado)
            method("inicio_testrun", resultado)
            method("duracion_testrun", resultado)
            method("id_configuraciones", resultado)
            method("nombre_configuraciones", resultado)
            method("deployado", resultado)
            method("resultado", resultado)
            method("abortados", resultado)
            method("completos", resultado)
            method("desconectados", resultado)
            method("errores", resultado)
            method("ejecutados", resultado)
            method("fallidos", resultado)
            method("en_progreso", resultado)
            method("inconclusos", resultado)
            method("no_ejecutados", resultado)
            method("no_ejecutables", resultado)
            method("pasados", resultado)
            method("pasados_abortados", resultado)
            method("pendientes", resultado)
            method("timeout", resultado)
            method("total", resultado)
            method("alertas", resultado)


if __name__ == '__main__':
    unittest.main()
