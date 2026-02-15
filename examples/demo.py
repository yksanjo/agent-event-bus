#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import AgentEventBus
def main():
    print("Agent Event Bus Demo")
    bus = AgentEventBus()
    bus.subscribe("test", lambda d: print(f"Got: {d}"))
    bus.publish("test", {"msg": "hello"})
    print("Done!")
if __name__ == "__main__": main()
