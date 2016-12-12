awesome-python3-webapp

The packages includes vagrant, ansilbe, docker, kubernetes yamls and awesome-python3-webapp, tests.

- Prerequsiste installation for local vagrant vm:

1. Git
2. Vagrant (plugin install vagrant-proxyconf + vagrant-vbguest)
3. Cygwin (rsync + ssh package) - for windows host only

- Setup for local vagrant vm & run awesome-python3-webapp, tests.:

1. open Cygwin window
2. git clone https://github.com/liujiatao/awesome-python3-webapp
3. vagrant up (ansible configuration)
4. vagrant ssh
5. python3.5 ./www/app.py or python3.5 ./www/app_test.py
