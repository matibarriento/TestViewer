#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
from xml.dom import minidom
from model import TestRun


TEMP_FILE_NAME = 'xml_temp.xml'


def ObtenerDatos(filename):

    resultado = TestRun()
    # trx_file = open(filename, 'r')
    xml_temp = open(TEMP_FILE_NAME, 'w')
    # for line in trx_file:
    #     xml_temp.write(line.replace('&#', ''))
    # trx_file.close()
    # xml_temp.close()
    # xmldoc = minidom.parse(TEMP_FILE_NAME)

    # Obtencion de datos del xml temporal

    resultado.nombre = 'Soy un bonito TST'

    # Limpieza de temporales
    if os.path.isfile(TEMP_FILE_NAME):
        os.remove(TEMP_FILE_NAME)

    return resultado
