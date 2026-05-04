class DecisionAnalytics:
    def __init__(self):
        self.decisions = []

    def record(self, decision_data: dict):
        self.decisions.append(decision_data)

    def metrics(self):
        total = len(self.decisions)
        if total == 0:
            return {}

        approvals = sum(1 for d in self.decisions if d["decision"] == "approved")
        overrides = sum(1 for d in self.decisions if d.get("overridden"))

        return {
            "total_decisions": total,
            "approval_rate": approvals / total,
            "override_rate": overrides / total,
            "avg_confidence": sum(d["confidence"] for d in self.decisions) / total,
        }
