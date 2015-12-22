#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import print_function
from model import TestRun
from modules import trx

trx_module = trx

print(trx_module.ObtenerDatos("").lista_test)
