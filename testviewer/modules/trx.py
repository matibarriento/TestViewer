#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
from xml.dom import minidom
# import xml.etree.ElementTree as ET
from utils import parseTIME
from model import TestRun


TEMP_FILE_NAME = 'xml_temp.xml'
TEST_PASADO_TEXTO = "Passed"


def ObtenerDatos(filename):
    resultado = TestRun()
    trx_file = open(filename, 'r')
    xml_temp = open(TEMP_FILE_NAME, 'w')
    for line in trx_file:
        xml_temp.write(line.replace('&#', ''))
    trx_file.close()
    xml_temp.close()
    xmldoc = minidom.parse(TEMP_FILE_NAME)

    #Obtencion de datos del Test Run

    testrun = xmldoc.getElementsByTagName("TestRun")[0]
    resultado.id_testrun = testrun.attributes["id"].value
    resultado.nombre_maquina_testrun = testrun.attributes["name"].value
    resultado.nombre_usuario_testrun = testrun.attributes["runUser"].value

    tiempos = testrun.getElementsByTagName("Times")[0]
    resultado.creacion_testrun = parseTIME(tiempos.attributes["creation"].value)
    resultado.finalizacion_testrun = parseTIME(tiempos.attributes["finish"].value)
    resultado.encolado_testrun = parseTIME(tiempos.attributes["queuing"].value)
    resultado.inicio_testrun = parseTIME(tiempos.attributes["start"].value)
    resultado.duracion_testrun = resultado.finalizacion_testrun - resultado.inicio_testrun

    configuraciones = testrun.getElementsByTagName("TestSettings")[0]
    resultado.id_configuraciones = configuraciones.attributes["id"]
    resultado.nombre_configuraciones = configuraciones.attributes["name"]
    deployado = configuraciones.getElementsByTagName("Deployment")[0]
    resultado.deployado = deployado.attributes["runDeploymentRoot"].value

    resumen = testrun.getElementsByTagName("ResultSummary")[0]
    resultado.resultado = resumen.attributes["outcome"].value
    numeros = resumen.getElementsByTagName("Counters")[0]
    resultado.abortados = numeros.attributes["aborted"].value
    resultado.completos = numeros.attributes["completed"].value
    resultado.desconectados = numeros.attributes["disconnected"].value
    resultado.errores = numeros.attributes["error"].value
    resultado.ejecutados = numeros.attributes["executed"].value
    resultado.fallidos = numeros.attributes["failed"].value
    resultado.en_progreso = numeros.attributes["inProgress"].value
    resultado.inconclusos = numeros.attributes["inconclusive"].value
    resultado.no_ejecutados = numeros.attributes["notExecuted"].value
    resultado.no_ejecutables = numeros.attributes["notRunnable"].value
    resultado.pasados = numeros.attributes["passed"].value
    resultado.pasados_abortados = numeros.attributes["passedButRunAborted"].value
    resultado.pendientes = numeros.attributes["pending"].value
    resultado.timeout = numeros.attributes["timeout"].value
    resultado.total = numeros.attributes["total"].value
    resultado.alertas = numeros.attributes["warning"].value

    # Limpieza de temporales
    if os.path.isfile(TEMP_FILE_NAME):
        os.remove(TEMP_FILE_NAME)

    return resultado
