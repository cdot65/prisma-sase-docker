FROM golang:alpine

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
LABEL name="ghcr.io/cdot65/pan-os-docker"
LABEL maintainer="cremsburg.dev@gmail.com"
LABEL description="Terraform container for Palo Alto Networks."
LABEL license="Apache 2.0"
LABEL url="https://github.com/cdot65/pan-os-docker"
LABEL build-date="20221126"

# ---------------------------------------------------------------------------
# Setup environment
# ---------------------------------------------------------------------------
ENV TERRAFORM_VERSION=1.3.6
ENV TF_DEV=true
ENV TF_RELEASE=true

WORKDIR /home/terraform

# ---------------------------------------------------------------------------
# Install dependencies
# ---------------------------------------------------------------------------
RUN apk add --update git bash openssh

# ---------------------------------------------------------------------------
# Install Terraform
# ---------------------------------------------------------------------------
WORKDIR $GOPATH/src/github.com/hashicorp/terraform
RUN git clone https://github.com/hashicorp/terraform.git ./ && \
    git checkout v${TERRAFORM_VERSION} && \
    /bin/bash scripts/build.sh