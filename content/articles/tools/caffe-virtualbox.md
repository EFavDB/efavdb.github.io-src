Title: Try Caffe pre-installed on a VirtualBox image
Date: 2016-03-22 15:02
Author: Cathy Yeh
Category: Tools
Tags: Caffe, deep learning, Jupyter, cloud
Slug: caffe-virtualbox
Status: published

A previous [post](http://efavdb.github.io/deep-learning-with-jupyter-on-aws) showed beginners how to try out deep learning libraries by

1.  using an Amazon Machine Image (AMI) pre-installed with deep learning libraries
2.  setting up a Jupyter notebook server to play with said libraries

If you have VirtualBox and [Vagrant](https://www.vagrantup.com/), you can follow a similar procedure on your own computer. The advantage is that you can develop locally, then deploy on an expensive AWS EC2 gpu instance when your scripts are ready.

For example, [Caffe](http://caffe.berkeleyvision.org/), the machine vision framework, allows you to seamlessly transition between cpu- and gpu-mode, and is available as a [vagrant box](https://atlas.hashicorp.com/malthejorgensen/boxes/caffe-deeplearning) running Ubuntu 14.04 ([**](#virtualization)64-bit), with Caffe pre-installed.

To add the box, type on the command line:
`vagrant box add malthejorgensen/caffe-deeplearning`

If you don't already have VirtualBox and Vagrant installed, you can find instructions online, or look at my [dotfiles](#vagrant_install) to get an idea.

* * * * *

Gotchas
-------

### SSH authentication failure

For me, the box had the wrong public key in `/home/vagrant/.ssh/authorized_keys file`, which gave me “authentication failure” upon starting up the box with `vagrant up`. This was fixed by:

Manually ssh into the box: `vagrant ssh`.

Then type (key taken from [here](https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub)):

```bash
echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key" > ~/.ssh/authorized_keys
```

Log out of the box, reload the box with `vagrant reload`, and hopefully the ssh authentication error is fixed.

### Jupyter notebook server

By default, the box has a notebook server on port 8003 that starts up from the /home/vagrant/caffe/examples directory, to be used in conjunction with port forwarding set in the Vagrant file:
`config.vm.network "forwarded_port", guest: 8003, host: 8003`
With the default setup, go to `http://localhost:8003` in your browser to access /home/vagrant/caffe/examples.

The default server setup limits access to only /home/vagrant/caffe/examples, so I prefer to set up my own configuration of the jupyter notebook server on port 8888 (allowing port forwarding of port 8888 in the Vagrantfile as well) and then start up the server from /home/vagrant, or wherever I'm working. To do this,

Log in to the box: `vagrant ssh`

Then create the notebook config file `~/.jupyter/jupyter_notebook_config.py` containing the following lines:

```
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888
```

### Vagrantfile

Here's the vagrant file that worked for me:

* * * * *



* Scripts to [install Virtualbox](https://github.com/frangipane/.dotfiles/blob/master/install/apt-get.sh) (line 31 and onwards) and [install Vagrant](https://github.com/frangipane/.dotfiles/blob/master/install/install-vagrant.sh).

** This is a 64-bit box, so you need to have Intel VT-x enabled in your BIOS.

   
