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
# Install dependencies and Python packages
# ---------------------------------------------------------------------------
RUN apk update
RUN apk --no-cache add curl gcc g++ graphviz
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
ADD requirements.txt /var/tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /var/tmp/requirements.txt

# ---------------------------------------------------------------------------
# Setup environment
# ---------------------------------------------------------------------------
WORKDIR /home/python
RUN ipython profile create paloalto
ADD ipython_config.py /root/.ipython/profile_paloalto/ipython_config.py
