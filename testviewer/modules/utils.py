#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from dateutil.parser import parse
from datetime import timedelta
import re


def parseTIME(string):
    return parse(string)


def parseTIMEDELTA(string):
    result = re.match(
        "(?P<hours>.+)\:(?P<minutes>.+)\:(?P<seconds>.+)\.(?P<milliseconds>.+)", string)
    return timedelta(hours=int(result.groupdict()["hours"]),
                     minutes=int(result.groupdict()["minutes"]),
                     seconds=int(result.groupdict()["seconds"]),
                     milliseconds=int(result.groupdict()["milliseconds"]))
