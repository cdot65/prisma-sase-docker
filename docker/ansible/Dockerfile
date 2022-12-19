FROM ghcr.io/cdot65/ansible-ee-paloaltonetworks:dev

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
LABEL name="ghcr.io/cdot65/pan-os-docker"
LABEL maintainer="cremsburg.dev@gmail.com"
LABEL description="Ansible container for Palo Alto Networks products."
LABEL license="Apache 2.0"
LABEL url="https://github.com/cdot65/pan-os-docker"
LABEL build-date="20221126"

# ---------------------------------------------------------------------------
# Add Python packages
# ---------------------------------------------------------------------------
ADD requirements.txt /var/tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /var/tmp/requirements.txt

# ---------------------------------------------------------------------------
# Setup environment
# ---------------------------------------------------------------------------
WORKDIR /home/ansible
RUN ansible-galaxy collection install paloaltonetworks.panos