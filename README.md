# prisma-sase-docker

[![N|Solid](./images/paloaltonetworks_logo.png)](https://www.paloaltonetworks.com/)

- [prisma-sase-docker](#prisma-sase-docker)
  - [`Overview`](#overview)
    - [Python Container Image](#python-container-image)
    - [Ansible Container Image](#ansible-container-image)

## `Overview`

The goal of this repository is to provide Docker containers for learning how to automate Palo Alto Networks Prisma products.

### Python Container Image

To use the Python container, you will use the `prisma-sase-docker:python` container tag. This container image will provide you with an interactive Python environment with the following additions:

- Prisma Access SDK (`panapi`) loaded
- Automatically form an authenticated session with Prisma upon container start

There is a requirement for a `config.yml` file on your machine, this file is used to authenticate with Prisma Access and is passed into our container during the `docker run` command. An example of this file can be found below.

```yaml
---
client_id: jennyjenny@8008675309.iam.panserviceaccount.com
client_secret: 18675309-abcd-abcd-abcd-18008675309
scope: profile tsg_id:8008675309 email
token_url: https://auth.apps.paloaltonetworks.com/am/oauth2/access_token
```

You can mount this file and gain access to container's Python REPL from the root of this project by typing the following command:

```bash
docker run -it -v $(pwd)/python/config.yml:/root/.panapi/config.yml ghcr.io/cdot65/prisma-sase-docker:python ipython --profile=paloalto
```

![python](images/docker_prisma_python.png)

### Ansible Container Image

If you'd like to use the Ansible container, you will use the `prisma-sase-docker:ansible` container tag. Using this container image will provide you with an interactive environment with these features:

- automatically provide the latest version of Prisma Access Ansible Collections
- provide necessary Python SDK library and dependencies

There is no need for a `config.yml` file with Ansible because the authentication variables will need to be passed into the playbook instead of loading them at run time. There are many ways of getting variables into Ansible playbooks, but the easiest way is to use a `group_vars` file. Here is an example project directory structure:

```shell
ansible-project
├── playbook.yaml
├── ansible.cfg
├── group_vars
│   └── all
│       └── authentication.yaml
└── inventory.yaml
```

The `group_vars/all/authentication.yaml` file will contain the following:

```yaml
---
client_id: "jennyjenny@8675309.iam.panserviceaccount.com"
client_secret: "18675309-5309-5309-5309-86753095309"
scope: "867530901"
```

It is _HIGHLY_ encouraged that you protect this file by encrypting it with Ansible Vault. You can learn more about Ansible Vault [here](docs/vault.md).

To run the Ansible container, you will need to mount your project directory into the container and set the working directory to the project directory. Here is an example command:

```bash
docker run -it --rm -v $(pwd):/ansible -w /ansible ghcr.io/cdot65/prisma-sase-docker:ansible
```

![ansible](images/docker_prisma_ansible.png)
