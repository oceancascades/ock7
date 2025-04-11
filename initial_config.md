# Setting up a new system (Ubuntu 24.04)

Setup ssh access and terminal. Aldo install some useful software packages. 

```
sudo apt install python3 python3-dev git curl net-tools openssh-client ssh
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
sudo ufw allow 22
```

### Install [TLJH](https://tljh.jupyter.org/en/latest/install/custom-server.html).

Remember to replace with your username!

```
curl -L https://tljh.jupyter.org/bootstrap.py | sudo -E python3 - --admin <admin-user-name>
```

Get the environments that I want to install

```
git clone https://github.com/oceancascades/conda_environments
```

### Install matlab with an offline license

Follow the [instructions](https://www.mathworks.com/help/install/ug/install-using-a-file-installation-key.html). May need to contact system admin to acquire an offline license file. 

Unzip the installer into a directory to avoid spewing files everywhere. 
```
unzip -d matlab matlab_R2024b_Linux.zip
```
