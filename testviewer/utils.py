#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import codecs

STATIC_RUTA = os.getcwd() + "/static/"


def AgregarJs(*args):
    contenedor = '<script type="text/javascript">\n{contenido}\n</script>'
    js = ""
    for arch in args:
        ruta_archivo = STATIC_RUTA + "js/" + arch
        if os.path.isfile(ruta_archivo):
            js = "{0} \n {1}".format(js, ArmarStatic(ruta_archivo))

    return contenedor.format(contenido=js)


def AgregarCSS(*args):
    contenedor = "<style>\n{contenido}\n</style>"
    css = ""
    for arch in args:
        ruta_archivo = STATIC_RUTA + "css/" + arch
        if os.path.isfile(ruta_archivo):
            css = "{0} \n {1}".format(css, ArmarStatic(ruta_archivo))
    return contenedor.format(contenido=css)


def ArmarStatic(ruta_archivo):
    with codecs.open(ruta_archivo, mode='r') as archivo:
        contenido = "\n".join(line.rstrip() for line in archivo)
        return contenido + "\n"
