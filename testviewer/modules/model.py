#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def ini(instance, propiedades):
    for prop in propiedades:
        instance.__dict__[prop] = None


class TestRun():

    """Modelo de la lista de test"""

    propiedades = {}

    def __init__(self):
        ini(self, TestRun.propiedades)


class TestClase():

    """Modelo de la clase de test"""

    propiedades = {}

    def __init__(self):
        ini(self, TestRun.propiedades)


class Test():

    """Model for Test"""

    propiedades = {}

    def __init__(self):
        ini(self, TestRun.propiedades)
