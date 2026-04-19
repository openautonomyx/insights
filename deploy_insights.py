#!/usr/bin/env python3
"""
Deployment Insights Module
Provides metrics and analytics for deployment tracking.
"""

import json
from datetime import datetime
from typing import Dict, List, Optional


class DeploymentInsights:
    """Track and analyze deployment metrics."""
    
    def __init__(self):
        self.deployments: List[Dict] = []
    
    def record_deployment(
        self,
        service: str,
        environment: str,
        version: str,
        status: str = "success",
        duration_seconds: Optional[float] = None
    ) -> Dict:
        """Record a deployment event."""
        deployment = {
            "id": len(self.deployments) + 1,
            "service": service,
            "environment": environment,
            "version": version,
            "status": status,
            "duration_seconds": duration_seconds,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.deployments.append(deployment)
        return deployment
    
    def get_metrics(self) -> Dict:
        """Calculate deployment metrics."""
        if not self.deployments:
            return {"total": 0}
        
        total = len(self.deployments)
        successful = sum(1 for d in self.deployments if d["status"] == "success")
        failed = total - successful
        
        return {
            "total": total,
            "successful": successful,
            "failed": failed,
            "success_rate": round(successful / total * 100, 2) if total > 0 else 0
        }
    
    def get_deployments_by_service(self, service: str) -> List[Dict]:
        """Get deployments for a specific service."""
        return [d for d in self.deployments if d["service"] == service]
    
    def to_json(self) -> str:
        """Export deployments as JSON."""
        return json.dumps(self.deployments, indent=2)


if __name__ == "__main__":
    # Demo usage
    insights = DeploymentInsights()
    
    # Record sample deployments
    insights.record_deployment("api", "production", "v1.2.0", "success", 45.2)
    insights.record_deployment("api", "production", "v1.2.1", "success", 52.1)
    insights.record_deployment("api", "production", "v1.2.2", "failed", 38.5)
    insights.record_deployment("web", "production", "v2.0.0", "success", 30.0)
    
    print("Deployment Insights")
    print("=" * 40)
    print(json.dumps(insights.get_metrics(), indent=2))