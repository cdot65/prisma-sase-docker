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
DOCKER_IMG = "ghcr.io/cdot65/pan-os-docker"

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
@task
def buildansible(context):
    """Build our Ansible Docker image."""
    context.run(
        f"docker build -t {DOCKER_IMG}:{ANSIBLE_TAG} docker/ansible",
    )


@task
def buildgolang(context):
    """Build our Golang Docker image."""
    context.run(
        f"docker build -t {DOCKER_IMG}:{GOLANG_TAG} docker/golang",
    )


@task
def buildpython(context):
    """Build our Python Docker image."""
    context.run(
        f"docker build -t {DOCKER_IMG}:{PYTHON_TAG} docker/python",
    )


@task
def buildterraform(context):
    """Build our Terraform Docker image."""
    context.run(
        f"docker build -t {DOCKER_IMG}:{TERRAFORM_TAG} docker/terraform",
    )


# ---------------------------------------------------------------------------
# ANSIBLE
# ---------------------------------------------------------------------------
@task
def ansible(context):
    """Get access to the ansible within our container."""
    context.run(
        f'docker run -it --rm \
            --mount type=bind,source="$(pwd)"/ansible,target=/home/ansible \
            -w /home/ansible/ \
            {DOCKER_IMG}:{ANSIBLE_TAG} ansible --version',
        pty=True,
    )


@task
def ansibleshell(context):
    """Get access to the shell within our container."""
    context.run(
        f'docker run -it --rm \
            --mount type=bind,source="$(pwd)"/ansible,target=/home/ansible \
            -w /home/ansible/ \
            {DOCKER_IMG}:{ANSIBLE_TAG} /bin/sh',
        pty=True,
    )


# ---------------------------------------------------------------------------
# GOLANG
# ---------------------------------------------------------------------------
@task
def golang(context):
    """Get access to the golang within our container."""
    context.run(
        f'docker run -it --rm \
            --mount type=bind,source="$(pwd)"/golang,target=/home/golang \
            -w /home/golang/ \
            {DOCKER_IMG}:{GOLANG_TAG} go version',
        pty=True,
    )


@task
def golangshell(context):
    """Get access to the shell within our golang container."""
    context.run(
        f'docker run -it --rm \
            --mount type=bind,source="$(pwd)"/golang,target=/home/golang \
            -w /home/golang/ \
            {DOCKER_IMG}:{GOLANG_TAG} /bin/sh',
        pty=True,
    )


# ---------------------------------------------------------------------------
# PYTHON
# ---------------------------------------------------------------------------
@task
def python(context):
    """Get access to the bpython REPL within our container."""
    context.run(
        f'docker run -it --rm \
            --mount type=bind,source="$(pwd)"/python,target=/home/python \
            -w /home/python/ \
            {DOCKER_IMG}:{PYTHON_TAG} ipython --profile=paloalto',
        pty=True,
    )


@task
def pythonshell(context):
    """Get access to the shell within our container."""
    context.run(
        f'docker run -it --rm \
            --mount type=bind,source="$(pwd)"/python,target=/home/python \
            -w /home/python/ \
            {DOCKER_IMG}:{PYTHON_TAG} /bin/sh',
        pty=True,
    )
