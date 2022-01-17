#!/usr/bin/python3
"""
    module
"""
from fabric.api import run, env, put, sudo, local
import os
from datetime import datetime

env.hosts = ['34.74.218.204', '34.138.156.219']


def do_clean(number=0):
    """ do_ clean """
    number = 1 if int(number) == 0 else int(number)
    outp = sudo("ls -1 /data/web_static/releases")
    print(outp.split('\n'))