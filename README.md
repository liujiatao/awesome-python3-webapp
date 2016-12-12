awesome-python3-webapp

The packages includes vagrant, ansilbe, docker, kubernetes yamls and awesome-python3-webapp, tests.

Prerequsiste for local vagrant vm:

Git
Vagrant (plugin install vagrant-proxyconf + vagrant-vbguest)
Cygwin (rsync + ssh package) - for windows host only
Setup for local vagrant vm & run awesome-python3-webapp, tests.:

open Cygwin window
git clone https://github.com/liujiatao/awesome-python3-webapp
vagrant up (ansible configuration)
vagrant ssh
python3.5 ./www/app.py or python3.5 ./www/app_test.py
