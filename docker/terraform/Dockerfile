FROM python:3.10-alpine

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
LABEL name="ghcr.io/cdot65/pan-os-docker"
LABEL maintainer="cremsburg.dev@gmail.com"
LABEL description="Python container for Palo Alto Networks SDK."
LABEL license="Apache 2.0"
LABEL url="https://github.com/cdot65/pan-os-docker"
LABEL build-date="20221126"

# ---------------------------------------------------------------------------
# Add and install python packages
# ---------------------------------------------------------------------------
ADD requirements.txt /var/tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /var/tmp/requirements.txt

# ---------------------------------------------------------------------------
# Setup environment
# ---------------------------------------------------------------------------
WORKDIR /home/python
RUN ipython profile create paloalto
ADD ipython_config.py /root/.ipython/profile_paloalto/ipython_config.py
