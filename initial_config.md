# Setting up a new system (Ubuntu 24.04)

Setup ssh access and terminal.
```
sudo snap install curl
sudo apt install git-all
bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/install.sh)"
sudo apt install openssh-client
sudo apt install ssh
sudo ufw allow 22
```

Install matlab with an offline license, follow the instructions:
https://www.mathworks.com/help/install/ug/install-using-a-file-installation-key.html

Unzip the installer into a directory
```
unzip -d matlab matlab_R2024b_Linux.zip
```

