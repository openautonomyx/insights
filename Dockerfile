FROM alpine:3.22

LABEL org.opencontainers.image.title="insights"
LABEL org.opencontainers.image.description="Container image for the insights content dataset"
LABEL org.opencontainers.image.source="https://github.com/${GITHUB_REPOSITORY}"

WORKDIR /data
COPY LICENSE README.md "Content Taxonomy 3.1.tsv" ./

CMD ["sh", "-c", "echo 'insights container contents:' && ls -lah /data"]
