#!/usr/bin/python3
"""
    module
"""
from fabric.api import run, env, put, sudo
import os

env.hosts = ['34.74.218.204', '34.138.156.219']


def do_deploy(archive_path):
    """ do_deploy """
    filename = archive_path.split('/')[-1][:-4]
    tmp_d = '/tmp/{}.tgz'.format(filename)
    rel_d = '/data/web_static/releases/' + filename + '/'
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        sudo('mkdir -p {}'.format(rel_d))
        sudo('tar -xzf {} -C {}'.format(tmp_d, rel_d))
        sudo('rm {}'.format(tmp_d))
        sudo('mv {}web_static/* {}'.format(rel_d, rel_d))
        sudo('rm -rf {}web_static'.format(rel_d))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {} /data/web_static/current'.format(rel_d))
        print('deployed')
        return True
    except BaseException as e:
        print(e)
        return False
