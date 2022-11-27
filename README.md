# pan-os-docker

[![N|Solid](./images/paloaltonetworks_logo.png)](https://www.paloaltonetworks.com/)

## `Overview`

The goal of this repository is to provide a Docker container for learning how to automate Palo Alto Networks products.

### Python

Python environment is provided by the `pan-os-docker:python` container tag. Using this container image will provide you with an interactive Python environment with the following additions:

- automatically load user variables from `./python/.env`
- Element Tree (from xml package) will be imported as ET
- all Python files stored within the [python](./python/) mounted at `/home/python`

### Ansible

All files related to Ansible are stored within the [ansible](./ansible/) directory at the root of this repository.

### Golang

All files related to Ansible are stored within the [golang](./golang/) directory at the root of this repository.

## ⚙️ `Building the containers`

After [ensuring that your environment is setup properly](./docs/environment.md), execute the build of your desired container with invoke.

```bash
invoke buildpython
invoke buildansible
invoke buildgolang
invoke buildterraform
```

## 🚀 `Run the container images`

Here are the following options for running your container of choice:

- `invoke python`
- `invoke golang`
- `invoke ansible`
- `invoke terraform`

## ⚙️ `How it works`

A quick guide on what is happening with this playbook will be [posted here](./docs/howitworks.md)
