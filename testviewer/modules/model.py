#!/usr/bin/env python2
# -*- coding: utf-8 -*-


class TestRun():

    """Modelo de la lista de test"""

    def __init__(self):
        self.listas_test = []
        self.clases_test = []
        self.tests = []

    def completar(self):
        self.duracion_testrun = self.finalizacion_testrun - self.inicio_testrun


class ClaseTest():

    """Modelo de la clase de test"""

    def __init__(self):
        self.tests = []

    def completar(self):
        self.exitosos = len(filter(lambda t: t.exitoso, self.tests))
        self.exitoso = len(self.tests) == self.exitosos
        self.duracion = 0
        if len(self.tests):
            self.duracion = reduce(
                lambda t1, t2: t1 + t2, [t.duracion for t in self.tests])


class ListaTest():

    """Modelo de la lista de tests"""

    def __init__(self):
        self.tests = []

    def completar(self):
        self.exitosos = len(filter(lambda t: t.exitoso, self.tests))
        self.exitoso = len(self.tests) == self.exitosos
        self.duracion = 0
        if len(self.tests):
            self.duracion = reduce(
                lambda t1, t2: t1 + t2, [t.duracion for t in self.tests])


class Test():

    """Modelo for Test"""

    def __init__(self):
        pass

    def completar(self, texto_exitoso):
        self.exitoso = self.resultado == texto_exitoso
