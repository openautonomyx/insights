# insights
Agentic Analysis Of Non Commercial Content Available on Web

## CI/CD and Container Publishing

This repository includes GitHub Actions workflows to:

- Validate Docker builds on pull requests and pushes to `main`.
- Build and publish Docker images to GitHub Container Registry (GHCR):
  - `ghcr.io/<owner>/<repo>`

### Workflows

- `CI` workflow: `.github/workflows/ci.yml`
  - Triggered on pull requests and pushes to `main`.
  - Builds the Docker image without pushing.

- `CD` workflow: `.github/workflows/cd.yml`
  - Triggered on pushes to `main`, version tags (`v*`), and manual dispatch.
  - Pushes images to GHCR.

### Registry Authentication

`GITHUB_TOKEN` is provided automatically by GitHub Actions and is used for GHCR publishing.

### Local Build + Push to GHCR

```bash
# login (requires a GitHub PAT with write:packages)
echo "$GITHUB_TOKEN" | docker login ghcr.io -u <github-username> --password-stdin

# build
docker build -t ghcr.io/<owner>/<repo>:local .

# push
docker push ghcr.io/<owner>/<repo>:local
```
