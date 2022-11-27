# Setting up your environment

This project requires Python and Docker to be installed on your local machine, an additional install of a 3rd party package called "invoke" will enable us to build an easy CLI for our work.

## Docker install

Follow the [official docs](https://docs.docker.com/get-docker/) to have Docker installed

## Python Virtual Environment creation

### With Poetry installed

I have included a `poetry` file for anyone saavy enough to take advantage. For the uninitiated, Poetry helps replicate Python environments between users with a single file. You'll need to have [Poetry installed on your machine](https://python-poetry.org/docs/), for most users that will be solved with `pip install poetry`.

Create your Python virtual environment:

```bash
poetry install
```

Activate your Python virtual environment:

```bash
poetry shell
```

### Without Poetry installed

Always, always, always strive to use virtual environments when working with Python. If you're needing a quick overview or refresher on Python virtual environments:

[Digital Ocean (macOS)](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos)
[Digital Ocean (Windows 10)](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

```bash
python3 -m venv venv
source venv/bin/activate
pip install invoke
```
