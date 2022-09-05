# Data_visualization_with_python

In this repo, we will learn how to use python to do basic data visualization. You can find all available tutorials under
[tutorials](tutorials)

## Set up a python dev env

### 1. Install pyenv

pyenv is is one of the coolest tool for managing multiple Python versions in your dev environment. Whether it’s your new machine learning venture or a full fledged product development initiative you will find pyenv super handy to setup your Python environments super fast and efficiently. So lets hop right into it.


```shell
sudo apt update -y

# install dependencies
apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl \
llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git


# get the source from the git repo
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

### 2. Configure Environment variables
Use the following commands to setup the PYENV_ROOT and PATH variables in .bashrc file of your Ubuntu.

```shell
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc 
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc 
```

Use the following commands to setup the pyenv init to initialize it. 

```shell
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
```

### 3. Restart your shell  and check the pyenv

```shell
# for bash user
exec bash
# or
exec "$SHELL"

# for  zsh
exec zsh

# check your pyenv existing python version and venv
pyenv versions

# below is an example output, system means the python of the system (e.g. ubuntu)
# the 3.9.13 is installed via pyenv, and a venv
  system
* 3.9.13 (set by /home/pliu/.pyenv/version)
  3.9.13/envs/venv-3.9.13
  venv-3.9.13

```

### Install multiple version of python

```shell
# list all available version
pyenv install --list

# install 3.10.1
pyenv install 310.1
```


### Install pyenv-virtualenv plugin

The new version of pyenv already has it by default, you don't need to install it explicitly

You can check all possible plugin

```shell
${pyenv_home}/plugins

# in my case
/home/pliu/.pyenv/plugins
```