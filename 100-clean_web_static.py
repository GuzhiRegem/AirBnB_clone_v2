#!/usr/bin/python3
"""
    module
"""
from fabric.api import run, env, put, sudo, local, cd, lcd
import os
from datetime import datetime

env.hosts = ['34.74.218.204', '34.138.156.219']


def do_clean(number=0):
    """ do_ clean """
    number = 1 if int(number) == 0 else int(number)
    comms = [
        'ls -1t versions',
        'grep "web_static"',
        "head -n{}".format(number)
    ]
    outp = local("|".join(comms), capture=True)
    lis = outp.split('\n')
    for ind, val in enumerate(lis):
        if val[-1] == "\r":
            lis[ind] = val[:-1]
    with lcd("versions"):
        sudo('rm -rv !("{}")'.format('"|"'.join(lis)))
    with cd("/data/web_static/releases/"):
        sudo('rm -rv !("{}")'.format('"|"'.join(lis)))
