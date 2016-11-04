from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
env.theme_path = 'themes'
DEPLOY_PATH = env.deploy_path
THEME_PATH = env.theme_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

def clean():
    if os.path.isdir(DEPLOY_PATH):
        local('rm -rf {deploy_path}'.format(**env))
        local('mkdir {deploy_path}'.format(**env))

def collectstatic():
    if os.path.isdir(DEPLOY_PATH):
        local('mkdir -p {deploy_path}/css/ {deploy_path}/js/ {deploy_path}/fonts/ {deploy_path}/images/'.format(**env))
        local('cp -rf {theme_path}/twenty/static/css/* {deploy_path}/css/'.format(**env))
        local('cp -rf {theme_path}/twenty/static/js/* {deploy_path}/js/'.format(**env))
        local('cp -rf {theme_path}/twenty/static/fonts/* {deploy_path}/fonts/'.format(**env))
        local('cp -rf {theme_path}/twenty/static/images/* {deploy_path}/images/'.format(**env))

def build():
    local('pelican content/ -s pelicanconf.py')
    collectstatic()

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican content/ -r -s pelicanconf.py')

def serve():
    local('cd {deploy_path} && python -m SimpleHTTPServer'.format(**env))

def reserve():
    build()
    serve()

def preview():
    local('pelican -s publishconf.py')

def cf_upload():
    rebuild()
    local('cd {deploy_path} && '
          'swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
          '-U {cloudfiles_username} '
          '-K {cloudfiles_api_key} '
          'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    local('pelican content/ -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True
    )
