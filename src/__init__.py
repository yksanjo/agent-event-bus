"""Agent Event Bus - Event bus for agent communication."""
from typing import Dict, List, Callable
from collections import defaultdict

class AgentEventBus:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = defaultdict(list)
    
    def subscribe(self, event: str, handler: Callable) -> None:
        self.subscribers[event].append(handler)
    
    def publish(self, event: str, data: dict) -> None:
        for h in self.subscribers[event]:
            h(data)

__all__ = ["AgentEventBus"]
