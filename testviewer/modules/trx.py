#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
from xml.dom import minidom
from utils import parseTIME, parseTIMEDELTA
from model import TestRun, Test, ListaTest, ClaseTest


TEMP_FILE_NAME = 'xml_temp.xml'
TEST_EXITOSO_TEXTO = "Passed"


def ObtenerDatos(filename):
    resultado = TestRun()
    trx_file = open(filename, 'r')
    xml_temp = open(TEMP_FILE_NAME, 'w')
    for line in trx_file:
        xml_temp.write(line.replace('&#', ''))
    trx_file.close()
    xml_temp.close()
    xmldoc = minidom.parse(TEMP_FILE_NAME)

    try:

        # Obtencion de datos del Test Run

        testrun = xmldoc.getElementsByTagName("TestRun")[0]
        resultado.id_testrun = testrun.attributes["id"].value
        resultado.nombre_maquina_testrun = testrun.attributes["name"].value
        resultado.nombre_usuario_testrun = testrun.attributes["runUser"].value

        tiempos = testrun.getElementsByTagName("Times")[0]
        resultado.creacion_testrun = parseTIME(tiempos.attributes["creation"].value)
        resultado.finalizacion_testrun = parseTIME(tiempos.attributes["finish"].value)
        resultado.encolado_testrun = parseTIME(tiempos.attributes["queuing"].value)
        resultado.inicio_testrun = parseTIME(tiempos.attributes["start"].value)

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

        # Obtencion de datos los Test
        lista_unit_test_result = testrun.getElementsByTagName("UnitTestResult")
        lista_unit_test = testrun.getElementsByTagName("UnitTest")
        lista_test_entry = testrun.getElementsByTagName("TestEntry")

        if not len(lista_unit_test_result) == len(lista_unit_test) == len(lista_test_entry):
            raise Exception("Incongruencia en cantidad de Test")

        cantidad = len(lista_unit_test_result)
        lista_clases = []

        for indice_test in range(0, cantidad):
            test = Test()
            unit_test_result = lista_unit_test_result[indice_test]
            unit_test = lista_unit_test[indice_test]
            test_entry = lista_test_entry[indice_test]
            if not (
                unit_test_result.attributes["testId"].value ==
                unit_test.attributes["id"].value ==
                test_entry.attributes["testId"].value
               ):
                    raise Exception("Incongruencia en ID de Test")

            # Obtencion de datos del Test

            test.id = unit_test_result.attributes["testId"].value
            test.computadora_test = unit_test_result.attributes["computerName"].value
            test.duracion = parseTIMEDELTA(unit_test_result.attributes["duration"].value)
            test.fin = parseTIME(unit_test_result.attributes["endTime"].value)
            test.id_ejecucion = unit_test_result.attributes["executionId"].value
            test.resultado = unit_test_result.attributes["outcome"].value
            test.resultado_id = unit_test_result.attributes["relativeResultsDirectory"].value
            test.inicio = parseTIME(unit_test_result.attributes["startTime"].value)
            test.id_lista = unit_test_result.attributes["testListId"].value
            test.nombre_test = unit_test_result.attributes["testName"].value
            test.tipo_test = unit_test_result.attributes["testType"].value
            metodo_test = unit_test.getElementsByTagName("TestMethod")[0]
            test.clase_test = metodo_test.attributes["className"].value.split(".")[-1]
            lista_clases.append(test.clase_test)

            if (len(unit_test_result.getElementsByTagName("Output")) > 0):
                msj = unit_test_result.getElementsByTagName("Message")[0]
                test.mensaje = msj.childNodes[0].nodeValue
                error = unit_test_result.getElementsByTagName("StackTrace")[0]
                test.error = error.childNodes[0].nodeValue
            else:
                test.mensaje = None
                test.error = None

            test.completar(TEST_EXITOSO_TEXTO)
            resultado.tests.append(test)

        lista_listas_test = testrun.getElementsByTagName("TestList")

        if len(lista_listas_test) > 0:
            for lista_test in lista_listas_test:
                lista = ListaTest()
                lista.id_lista = lista_test.attributes["id"].value
                lista.nombre_lista = lista_test.attributes["name"].value
                lista.tests = filter(lambda t: t.id_lista == lista.id_lista, resultado.tests)

                lista.completar()
                resultado.listas_test.append(lista)

        if len(lista_clases) > 0:
            for clase_test in lista_clases:
                clase = ClaseTest()
                clase.nombre_clase = clase_test
                clase.tests = filter(lambda t: t.clase_test == clase_test, resultado.tests)
                clase.completar()
                resultado.clases_test.append(clase)

    except Exception as e:
        raise e
    finally:
        # Limpieza de temporales
        if os.path.isfile(TEMP_FILE_NAME):
            os.remove(TEMP_FILE_NAME)

    resultado.completar()
    return resultado
