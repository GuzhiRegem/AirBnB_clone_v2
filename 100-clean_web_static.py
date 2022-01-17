#!/usr/bin/python3
"""
    module
"""
from fabric.api import run, env, put, sudo, local, cd, lcd

env.hosts = ['34.74.218.204', '34.138.156.219']


def do_clean(number=0):
    """
    do_clean
    """
    number = 1 if int(number) == 0 else int(number)
    comms = [
        'ls -1t',
        'grep "web_static"',
        "head -n{}".format(number)
    ]
    try:
        with lcd("versions"):
            lis = local(" | ".join(comms), capture=True).split('\n')
            for ind, val in enumerate(lis):
                lis[ind] = val[:-1] if val[-1] == "\r" else val
            l_lis = local(" | ".join(comms[:-1]), capture=True).split('\n')
            for ind, val in enumerate(l_lis):
                l_lis[ind] = val[:-1] if val[-1] == "\r" else val
            for a in l_lis:
                if a not in lis:
                    local('rm -r {}'.format(a))
        with cd("/data/web_static/releases/"):
            l_lis = sudo(" | ".join(comms[:-1])).split('\n')
            for ind, val in enumerate(l_lis):
                l_lis[ind] = val[:-1] if val[-1] == "\r" else val
            for a in l_lis:
                if a not in lis:
                    sudo('rm -r {}'.format(a))
        return True
    except Exception:
        return False
