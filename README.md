# insights
Agentic Analysis Of Non Commercial Content Available on Web

## CI/CD and Container Publishing

This repository now includes GitHub Actions workflows to:

- Validate Docker builds on pull requests and pushes to `main`.
- Build and publish Docker images to:
  - GitHub Container Registry (GHCR): `ghcr.io/<owner>/<repo>`
  - Docker Hub: `<dockerhub-username>/<repo>`

### Workflows

- `CI` workflow: `.github/workflows/ci.yml`
  - Triggered on pull requests and pushes to `main`.
  - Builds the Docker image without pushing.

- `CD` workflow: `.github/workflows/cd.yml`
  - Triggered on pushes to `main`, version tags (`v*`), and manual dispatch.
  - Pushes images to GHCR and Docker Hub.

### Required GitHub Secrets

Set the following repository secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

`GITHUB_TOKEN` is provided automatically by GitHub Actions and is used for GHCR publishing.

### Local Build

```bash
docker build -t insights:local .
docker run --rm insights:local
```
