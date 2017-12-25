# -*- coding: utf-8 -*-
"""
@author: redstar
"""
from fabric.api import env, sudo, cd, run, local, put  #@UnresolvedImport

# ssh user
env.user = "root"
env.hosts = ["52.74.116.89"]

APP_ROOT = '/data/Mintegral_API_Test'

def bootstrap():
    sudo('mkdir -p %s' % APP_ROOT)
    sudo('chown %s %s' % (env.user, APP_ROOT))

    with cd( APP_ROOT ):
        run( 'virtualenv venv' )

def pack():
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    dist = local( 'python setup.py --fullname', capture=True ).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/%s.tar.gz' % dist)

    with cd("/tmp/"):
        run( 'tar zxvf /tmp/%s.tar.gz' % dist )
        with cd( dist ):
            run( '%s/venv/bin/python setup.py install' % ( APP_ROOT ) )
            run( 'cp -f runtest.py %s' % APP_ROOT)

    run( 'rm -rf /tmp/%s /tmp/%s.tar.gz' % (dist,dist) )

def runtest():
    with cd( APP_ROOT ):
        run( '. venv/bin/activate && rm -rf reports && python runtest.py' )
