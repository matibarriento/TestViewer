#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import logging
import os
import sys
from jinja2 import FileSystemLoader, Environment
from utils import AgregarJs, AgregarCSS
from modules import trx

templateLoader = FileSystemLoader(searchpath=os.getcwd() + "/templates")
templateEnv = Environment(loader=templateLoader)
templateEnv.globals['AgregarJs'] = AgregarJs
templateEnv.globals['AgregarCSS'] = AgregarCSS


def Generar(filepath, nombre_reporte="reporte", nombre_template="default.html"):
    reload(sys)
    sys.setdefaultencoding("utf-8")

    filename, file_extension = os.path.splitext(filepath)
    if file_extension.lower() == ".trx":
        trx_module = trx
        resultado = trx_module.ObtenerDatos(filepath)
    else:
        raise Exception("Archivo invalido")
    template = templateEnv.get_template(nombre_template)
    informe = open(nombre_reporte + '.html', 'w')
    informe.write(template.render({"resultado": resultado}))
    informe.close()

if __name__ == "__main__":
    # fileName = sys.argv[1]
    path_archivo = "/home/matibarriento/Downloads/TestResultFailed.trx"
    Generar(path_archivo)
