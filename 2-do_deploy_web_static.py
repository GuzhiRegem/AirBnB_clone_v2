#!/usr/bin/python3
"""
    module
"""
from fabric.api import run, env, put
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
        run('mkdir -p {}'.format(rel_d))
        run('tar -xzf {} -C {}'.format())
        run('rm {}'.format(tmp_d))
        run('mv {}web_static/* {}'.format(rel_d, rel_d))
        run('rm -rf {}web_static'.format(rel_d))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(rel_d))
        print('deployed')
        return True
    except BaseException:
        return False
