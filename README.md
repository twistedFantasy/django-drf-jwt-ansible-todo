# django-drf-jwt-todo

The Goal of this app is to provide good and clear example of usage the power of Python and Django/Django Rest Framework together with 
additional 3-rd party packages to create a simple TODO application. And of course ansible one love!

# Versions
```
Python: 3.7.3
Django: 2.2.2
Django Rest Framework: 3.9.4
PostgreSQL: 11
VirtualBox: 5.2.22
Ansible: 2.8.0
etc...
```

# Configuration
Start new virtualbox machine(ubuntu 19.04) with installed ansible by vagrant
``` 
% vagrant up
```
SSH to virtual machine
```
% vagrant ssh
```
Go to shared between host and virtual machine directory
```
% cd /vagrant_data/django-drf-jwt-ansible-todo
```
Configure project and install all needed dependencies with ansible-playbook
``` 
% cd /vagrant_data/django-drf-jwt-ansible-todo/ansible
% ansible-playbook playbooks/todo/main.yml 
```
To run playbook with selected tags
``` 
% ansible-playbook playbooks/todo/main.yml --tags=settings
```
Start django development server
``` 
% cd /vagrant_data/django-drf-jwt-ansible-todo/todo
% python3 manage.py runserver 0.0.0.0:8000
```
Access Django admin page in browser
```
http://192.168.33.59:8000/admin/
```

# Ansible-galaxy
Install needed dependencies from Ansible Galaxy or github directly. The `--force` is needed to force version upgrades.
``` 
% ansible-galaxy install -r requirements.yml --force
```
