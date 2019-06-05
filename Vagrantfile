# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/disco64"
  config.ssh.forward_agent = false
  config.vm.box_check_update = false

  config.vm.network "private_network", ip: "192.168.33.59"
  config.vm.synced_folder ".", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--name", "TestApp", "--memory", "4040"]
  end

  config.vm.provision "shell", inline: <<-SHELL
    # ansible
    apt update
    apt install -y software-properties-common
    apt-add-repository ppa:ansible/ansible
    apt update
    apt install -y ansible
  SHELL
end
