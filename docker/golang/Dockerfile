FROM golang:1.16-alpine

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
LABEL name="ghcr.io/cdot65/prisma-sase-docker"
LABEL maintainer="cremsburg.dev@gmail.com"
LABEL description="Golang container for Palo Alto Networks SDK."
LABEL license="Apache 2.0"
LABEL url="https://github.com/cdot65/prisma-sase-docker"
LABEL build-date="20221126"

# ---------------------------------------------------------------------------
# Add and install golang packages
# ---------------------------------------------------------------------------
WORKDIR /home/golang
RUN apk add git
# RUN git clone https://github.com/PaloAltoNetworks/pango.git
RUN go get github.com/PaloAltoNetworks/pango
