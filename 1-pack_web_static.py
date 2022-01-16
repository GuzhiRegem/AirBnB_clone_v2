#!/usr/bin/python3
"""
    module
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """ do_ pack """
    tim = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions')
    local('tar -cvzf "versions/web_static_{}.tgz" web_static'.format(tim))
