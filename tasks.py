"""Tasks for use with Invoke.

(c) 2021 Calvin Remsburg
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import os
from invoke import task

# ---------------------------------------------------------------------------
# DOCKER PARAMETERS
# ---------------------------------------------------------------------------
DOCKER_IMG = "ghcr.io/cdot65/prisma-sase-docker"

PYTHON_TAG = "python"
ANSIBLE_TAG = "ansible"
TERRAFORM_TAG = "terraform"
GOLANG_TAG = "golang"


# ---------------------------------------------------------------------------
# SYSTEM PARAMETERS
# ---------------------------------------------------------------------------
PWD = os.getcwd()


# ---------------------------------------------------------------------------
# DOCKER CONTAINER BUILDS
# ---------------------------------------------------------------------------
@task(optional=["ansible", "go", "python", "terraform"])
def build(context, ansible=None, go=None, python=None, terraform=None):
    """Build our Docker images."""
    if ansible:
        context.run(
            f"docker build -t {DOCKER_IMG}:{ANSIBLE_TAG} docker/ansible",
        )
    elif go:
        context.run(
            f"docker build -t {DOCKER_IMG}:{GOLANG_TAG} docker/golang",
        )
    elif python:
        context.run(
            f"docker build -t {DOCKER_IMG}:{PYTHON_TAG} docker/python",
        )
    elif terraform:
        context.run(
            f"docker build -t {DOCKER_IMG}:{TERRAFORM_TAG} docker/terraform",
        )
    else:
        context.run("echo 'invoke build --ansible, --go, --python, or --terraform ?'")


# ---------------------------------------------------------------------------
# SHELL ACCESS
# ---------------------------------------------------------------------------
@task(optional=["ansible", "go", "python", "terraform"])
def shell(context, ansible=None, go=None, python=None, terraform=None):
    """Get shell access to the container."""
    if ansible:
        context.run(
            f'docker run -it --rm \
                --mount type=bind,source="$(pwd)"/ansible/.vault_pass,target=/home/runner/.vault_pass \
                --mount type=bind,source="$(pwd)"/ansible,target=/ansible \
                -w /ansible \
                {DOCKER_IMG}:{ANSIBLE_TAG}',
            pty=True,
        )
    elif python:
        context.run(
            f'docker run -it --rm \
                --mount type=bind,source="$(pwd)"/python/config.yml,target=/root/.panapi/config.yml \
                --mount type=bind,source="$(pwd)"/python,target=/home/python \
                -w /home/python/ \
                {DOCKER_IMG}:{PYTHON_TAG} /bin/sh',
            pty=True,
        )
    else:
        context.run("echo 'invoke shell --ansible, --go, --python, or --terraform ?'")


# ---------------------------------------------------------------------------
# PYTHON
# ---------------------------------------------------------------------------
@task
def python(context):
    """Get access to the ipython REPL within our container."""
    context.run(
        f"docker run -it --rm \
            --mount type=bind,source=$HOME/.panapi/config.yml,target=/root/.panapi/config.yml \
            {DOCKER_IMG}:{PYTHON_TAG} ipython --profile=paloalto",
        pty=True,
    )
