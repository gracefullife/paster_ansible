=========================================
paster_ansible
=========================================


How to 
=========================================

Installation
--------------------

pip install git+https://github.com/gracefullife/paster_ansible.git

Use
--------------------

paster create -t ansible project_name



Customizing
=========================================

git clone and put customized files to paster_ansible/templates/default_project/  if you want to customize template.

after this, use command below

make egg    
  or
python setup.py bdist_egg

easy_install dist/paster_ansible-0.1dev_r0-py2.7.egg

