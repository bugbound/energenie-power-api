###############
### imports ###
###############

from fabric.api import cd, lcd, put, sudo, warn_only

import logging;

logging.getLogger('paramiko.transport').addHandler(logging.StreamHandler())
##############
### config ###
##############

local_app_dir = './power-api'
remote_app_dir = '/opt/power-api'
supervisor_task = 'power_api'

#############
### tasks ###
#############


	
def start():
	sudo('supervisorctl start %s'%supervisor_task)		


def stop():
	with warn_only():
		sudo('supervisorctl stop %s'%supervisor_task)


	
def setup():
	sudo('mkdir -p %s'%remote_app_dir)
	sudo('apt install git python-rpi.gpio -y -q')
	sudo('apt install gunicorn python-pip supervisor -y -q')
	sudo('pip -q install flask')
	sudo('mkdir -p /etc/supervisor/conf.d/')
	put('supervisord.conf', '/etc/supervisor/conf.d/power-api.supervisord.conf', use_sudo=True)	
	sudo('chown pi.pi %s -R'%remote_app_dir)
	sudo('supervisorctl update')
	
def deploy():
	stop()
	sudo('mkdir -p %s'%remote_app_dir)
	with lcd(local_app_dir):
		with cd(remote_app_dir):
			put('*', './', use_sudo=True)
	start()

def reboot():
	with warn_only():
		sudo('reboot')
