# Setting up a new system (Ubuntu 24.04)

Setup ssh access and terminal. Also install some useful software packages. 

```
sudo apt install python3 python3-dev git curl net-tools openssh-client ssh vim
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
sudo ufw allow 22
```

Set the hostname to something we want.

```
sudo hostnamectl set-hostname newhostname
```

Also edit `/etc/hosts` to include the new hostname and then restart the system to make sure it updates. 

### Install [TLJH](https://tljh.jupyter.org/en/latest/install/custom-server.html).

Using their installer script should be easy, just replace the admin usename as appropriate.

```
curl -L https://tljh.jupyter.org/bootstrap.py | sudo -E python3 - --admin <admin-user-name>
```

However, if this fails (as it did on a new install recently, try 'the hard way').

Get the environments that I want to install

```
git clone https://github.com/oceancascades/conda_environments
```

Then you need to add them as `sudo` which manual path to the conda binary. 

### Install JupyterHub the hard way

https://github.com/jupyterhub/jupyterhub-the-hard-way/blob/HEAD/docs/installation-guide-hard.md

I followed the instructions to the letter down to the conda environments section. In the configuration I enabled access to all users that could authenticate:

```
c.Authenticator.allow_all = True
```
I also uncommented

```
c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
```

I did not install the environments as suggested either. Instead I get the environments that I want to install from github.

```
git clone https://github.com/oceancascades/conda_environments
```

And install them using

```
sudo /opt/conda/bin/conda env create --prefix /opt/conda/envs/multitool -f multitool.yml
sudo /opt/conda/envs/multitool/bin/python -m ipykernel install --prefix /usr/local/ --name 'multitool' --display-name "multitool"
sudo /opt/conda/bin/conda env create --prefix /opt/conda/envs/arrr -f arrr.yml
```

Installing the R kernel was a pain. I had to figure out how to place it manually in the correct path. The easiest way to do this was to setup an R kernel on another system using the [standard proceedure](https://github.com/IRkernel/IRkernel), find the directory where it was stored using `jupyter kernelspec list`, and then copy the directory to the appropriate location on the new linux system, which in my case was:

```
/usr/local/share/jupyter/kernels/
```

At this point you can manually edit the `kernel.json` file to point to the appropriate `R` binary that was installed into the conda environment. For me this was

```
/opt/conda/envs/arrr/bin/R
```


### Install matlab with an offline license

Follow the [instructions](https://www.mathworks.com/help/install/ug/install-using-a-file-installation-key.html). 

To acquire an offline license file I had to contact my system admin and provide a hostid (the computer MAC address, acquired using `ifconfig`) and the computer name and the version of MATLAB needed.

Unzip the installer into a directory to avoid spewing files everywhere. 
```
unzip -d matlab matlab_R2024b_Linux.zip
```

There is a bug in the matlab GUI so you might need to delete your default network gateway (kind of crazy!). 


### Mounting an SMB share for all users

```
sudo apt install cifs-utils
sudo mkdir /mnt/sharename
```

Make an `fstab` entry:

```
//server/sharename /mnt/sharename cifs guest,uid=1000,gid=1000,iocharset=utf8 0 0
```

replacing server and sharename as appropriate.
