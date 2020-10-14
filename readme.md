# Aubergina

Aubergina Password Manager

## Setup Development Environment

- Clone this repo: `git clone git@git.sindria.org:dorjecurreli/aubergina.git`
- Move into it: `cd aubergina`
- Build local image: `bash build.sh registry.sindria.org/dorjecurreli/aubergina local`
- Setup env: `cp .env.local .env`
- Setup docker compose: `cp docker-compose.local.yml docker-compose.yml`
- Start environment: `docker-compose up -d`
