#!/usr/bin/python3
"""
    module
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ do_ pack """
    try:
        tim = datetime.now().strftime('%Y%m%d%H%M%S')
        name = "versions/web_static_{}.tgz".format(tim)
        local('mkdir -p versions')
        local('tar -cvzf "{}" web_static'.format(name))
        return name
    except Exception:
        return None
