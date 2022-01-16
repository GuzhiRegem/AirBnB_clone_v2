#!/usr/bin/python3
"""
    module
"""
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """ deploy """
    ret = do_pack()
    if not ret:
        return False
    return do_deploy(ret)
