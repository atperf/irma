"""Simple AI agent placeholder for suggesting ticket templates and updating KPIs."""
from typing import List


class AIAgent:
    def suggest_templates(self, history: List[str]) -> List[str]:
        # In production this would call OpenAI or other LLM
        return ["8D" if "8D" in h else "5W" for h in history]
