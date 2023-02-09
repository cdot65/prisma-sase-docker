# prisma-sase-docker

[![N|Solid](./images/paloaltonetworks_logo.png)](https://www.paloaltonetworks.com/)

## `Overview`

The goal of this repository is to provide Docker containers for learning how to automate Palo Alto Networks Prisma products.

### Python

Python environment is provided by the `prisma-sase-docker:python` container tag. Using this container image will provide you with an interactive Python environment with the following additions:

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

![invoke python](images/docker_prisma_python.png)

### Ansible

An Ansible environment is provided by the `prisma-sase-docker:ansible` container tag. Using this container image will provide you with an interactive environment with the following additions:

- automatically provide the latest version of Prisma Access Ansible Collections
- provide necessary Python SDK library and dependencies

If you would like to execute Ansible playbooks within the your workstation's [ansible](./ansible/) directory, you will find them mounted at `/home/ansible` within the container's shell, which can be accessed with:

```bash
docker run -it --rm -v $(pwd):/ansible -w /ansible ghcr.io/cdot65/prisma-sase-docker:ansible
```
