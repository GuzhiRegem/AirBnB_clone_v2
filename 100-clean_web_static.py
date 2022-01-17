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
    comms = [
        'ls -1t /data/web_static/releases',
        'grep "web_static"',
        "head -n{}".format(number)
    ]
    outp = sudo("|".join(comms))
    lis = outp.split('\n')
    for ind, val in enumerate(lis):
        if val[-1] == "\r":
            lis[ind] = val[:-1]
    sudo('rm -rv /data/web_static/releases/!("{}")'.format('"|"'.join(lis)))
    sudo('rm -rv versions/!("{}")'.format('"|"'.join(lis)))
    