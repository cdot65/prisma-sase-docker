FROM ghcr.io/cdot65/ansible-ee-prismasase:0.1.4

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
LABEL name="ghcr.io/cdot65/prisma-sase-docker"
LABEL maintainer="cremsburg.dev@gmail.com"
LABEL description="Ansible container for Palo Alto Networks Prisma SASE."
LABEL license="Apache 2.0"
LABEL url="https://github.com/cdot65/prisma-sase-docker"
LABEL build-date="20230209"

# ---------------------------------------------------------------------------
# Set up environment
# ---------------------------------------------------------------------------
ENV TERM xterm
ENV ZSH_THEME cloud

RUN dnf install -y zsh wget 
RUN dnf clean all
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

# ---------------------------------------------------------------------------
# Add Python packages
# ---------------------------------------------------------------------------
ADD requirements.txt /var/tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /var/tmp/requirements.txt

# ---------------------------------------------------------------------------
# Setup environment
# ---------------------------------------------------------------------------
WORKDIR /home/runner

# start zsh
CMD [ "zsh" ]
