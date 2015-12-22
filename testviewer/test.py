#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function
import unittest
from model import TestRun
from modules import trx


class TestModulos(unittest.TestCase):

    """docstring for TestModulos"""

    def test_trx_modulo(self):

        path_archivo = ""
        trx_module = trx
        resultado = trx_module.ObtenerDatos(path_archivo).__dict__
        print(resultado)
        self.assertIn("nombre", resultado)
        self.assertGreater(0, len(resultado["lista_test"]))


if __name__ == '__main__':
    unittest.main()
