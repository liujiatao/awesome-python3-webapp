# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
config.vm.box = "centos/7"
  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
config.vm.box_check_update = false
config.ssh.insert_key = false

config.vm.network "private_network", ip: "10.100.199.200"
  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
#config.vm.network "public_network",
#ip: "16.173.244.55",
#use_dhcp_assigned_default_route: true
  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
#config.vm.synced_folder ".", "/home/vagrant" , disabled:true
config.vm.synced_folder ".", "/vagrant"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: "sed -i 's#PasswordAuthentication no#PasswordAuthentication yes#g' /etc/ssh/sshd_config"
  config.vm.provision "shell", inline: "service sshd restart"
  config.vm.provision "shell", inline: "yum -y install https://centos7.iuscommunity.org/ius-release.rpm"
  config.vm.provision "shell", inline: "yum -y install ansible"
  #config.vm.provision "shell", inline: "tar -xf /vagrant/ansible.tar"
  config.vm.provision "shell", inline: "ansible-playbook -i /vagrant/ansible/hosts /vagrant/ansible/site.yml -c local"
  
 # config.vbguest.auto_update = false
  if Vagrant.has_plugin?("vagrant-cachier")
    config.cache.scope = :box
  end
 # the proxy is used for my company env 
  if Vagrant.has_plugin?("vagrant-proxyconf")
    config.proxy.http     = "http://web-proxy.corp.hp.com:8080"
    config.proxy.https    = "http://web-proxy.corp.hp.com:8080/"
    config.proxy.no_proxy = "localhost,127.0.0.1,.example.com"
  end
end
