from typing import Dict, Any, List


class InsightEngine:
    """
    Transforms raw agent output into structured, decision-grade insights.
    This is the CORE of your product.
    """

    def analyze(self, agent_output: str, context: Dict[str, Any] = None) -> Dict:
        """
        Convert unstructured LLM output into structured decision intelligence.
        """
        context = context or {}

        decision = self._extract_decision(agent_output)
        confidence = self._estimate_confidence(agent_output)
        risk = self._assess_risk(agent_output, context)

        return {
            "decision": decision,
            "confidence": confidence,
            "risk_level": risk,
            "requires_human": risk in ["medium", "high"],
            "recommended_action": self._recommend_action(risk),
            "reasoning": self._extract_reasoning(agent_output),
        }

    def _extract_decision(self, text: str) -> str:
        if "approve" in text.lower():
            return "approved"
        if "reject" in text.lower():
            return "rejected"
        return "unknown"

    def _estimate_confidence(self, text: str) -> float:
        length = len(text.split())
        return min(0.5 + (length / 200), 0.95)

    def _assess_risk(self, text: str, context: Dict[str, Any]) -> str:
        if "urgent" in text.lower() or "high impact" in text.lower():
            return "high"
        if "budget" in text.lower():
            return "medium"
        return "low"

    def _recommend_action(self, risk: str) -> str:
        return {
            "low": "auto-approve",
            "medium": "manager-review",
            "high": "escalate",
        }[risk]

    def _extract_reasoning(self, text: str) -> List[str]:
        return [line.strip() for line in text.split(".") if line.strip()]
