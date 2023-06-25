# python-devops (Guide)
From scratch repository up to doing Python DevOps work.

## Scope:
### Project scaffold

Cloud-based Dev environments:
#### Colab Notebook
  - This is an example of how to integrate [colab](https://github.com/endybits/python-devops/blob/master/data_structures_and_more.ipynb) into your github projects, as a cloud-based environment option.

#### GitHub Codespaces
* Makefile
* Requirements.txt
* test_lib.py
* Dockerfile
* Microservice

1. Create virtualenv `python -m venv ~/.venv`
2. Edit my `~/.bashrc` to run virtuaenv every time the terminal is opened: including the code `source ~/venv/bin/activate` in the last line.

#### AWS CloudShell

#### AWS Cloud9
To clone your repo here you need to create a ssh-keygen `ssh-keygen -t rsa` and include the public key in your github settings. 
Also, you need to create your own virtualenv because the default virtual virtualenv of cloud9 has many dependencies that you won't require in your project.

1. Create virtualenv `python3 -m venv ~/.venv`
2. Edit my `~/.bashrc` to run virtuaenv every time the terminal is opened: including the code `source ~/venv/bin/activate` in the last line.


### Command-line tools
### Microservices
### Containerized CD
