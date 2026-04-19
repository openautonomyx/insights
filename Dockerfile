FROM python:3.12-alpine

LABEL org.opencontainers.image.title="insights"
LABEL org.opencontainers.image.description="Container image for the insights content dataset"
LABEL org.opencontainers.image.source="https://github.com/${GITHUB_REPOSITORY}"

WORKDIR /data
COPY LICENSE README.md content_taxonomy.tsv deploy_insights.py ./

EXPOSE 8080

CMD ["python3", "-c", "from deploy_insights import DeploymentInsights; i = DeploymentInsights(); i.record_deployment('api', 'production', 'v1.0.0', 'success', 45.2); print(i.get_metrics())"]
